import henge
import json
import logging
import logmuse
import os
import refget
import uvicorn
import sys

from fastapi import Body, FastAPI, Response
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from platform import python_version
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from typing import Union
from ubiquerg import VersionInHelpParser

from .cli import build_parser
from .scconf import RDBDict, SeqColConf
from ._version import __version__ as seqcolapi_version
from .examples import *

from refget._version import __version__ as refgetclient_version
from seqcol._version import __version__ as seqcol_version
from seqcol import SeqColClient

global _LOGGER

_LOGGER = logging.getLogger(__name__)
# _LOGGER.setLevel(logging.DEBUG)

PKG_NAME = "seqcolapi"
ALL_VERSIONS = {
    "server_version": seqcolapi_version,
    "seqcol_version": seqcol_version,
    "refget_client_version": refgetclient_version,
    "python_version": python_version(),
}
STATIC_DIRNAME = "static"
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), STATIC_DIRNAME)
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
templates = Jinja2Templates(directory=TEMPLATES_PATH)

_LOGGER.info(ALL_VERSIONS)

app = FastAPI(
    title="Sequence Collections API",
    description="An API providing metadata such as names, lengths, and other values for collections of reference sequences",
    version=seqcolapi_version,
)

app.mount("/" + STATIC_DIRNAME, StaticFiles(directory=STATIC_PATH), name=STATIC_DIRNAME)

@app.get(
    "/status", name="Status", summary="Check server status", tags=["General endpoints"]
)
async def root():
    return Response(content="Welcome to the test seqcol server.")


@app.get("/service-info", summary="GA4GH service info", tags=["General endpoints"])
async def root():
    return Response(content="Service info")


@app.get("/", summary="Home page", tags=["General endpoints"])
async def index(request: Request):
    """
    Returns a landing page HTML with the server resources ready to download. No inputs required.
    """
    templ_vars = {"request": request, "openapi_version": app.openapi()["openapi"]}
    _LOGGER.debug("merged vars: {}".format(dict(templ_vars, **ALL_VERSIONS)))
    return templates.TemplateResponse("index.html", dict(templ_vars, **ALL_VERSIONS))


@app.get(
    "/sequence/{digest}",
    summary="Retrieve raw sequence via refget protocol",
    tags=["General endpoints"],
)
async def root(digest: str=example_sequence):
    return Response(content=scclient.refget(digest))


@app.get(
    "/collection/{digest}",
    summary="Retrieve a sequence collection",
    tags=["Retrieving sequence collections"],
)
async def collection_recursive(digest: str=example_digest, level: Union[int, None] = None):
    print("retriving collection")
    if level == None:
        level = 2
    if level > 2:
        return Response(
            content="Error: recursion > 1 disabled. Use the /refget server to retrieve sequences."
        )
    try:
        return JSONResponse(content=scclient.retrieve(digest, reclimit=level-1))
    except:
        return {}


@app.get(
    "/comparison/{digest1}/{digest2}",
    summary="Compare two sequence collections hosted on the server",
    tags=["Comparing sequence collections"],
)
async def compare2digests(
    digest1: str = example_digest_hg38, digest2: str = example_digest_hg38_primary
):
    _LOGGER.info("Compare called")
    result = {}
    result["digests"] = {
        "a": digest1,
        "b": digest2
    }
    result.update(scclient.compare_digests(digest1, digest2))
    return JSONResponse(result)


@app.post(
    "/comparison/{digest1}",
    summary="Compare a local sequence collection to one on the server",
    tags=["Comparing sequence collections"],
)
async def compare1digest(digest1: str = example_digest_hg38, B: dict = example_hg38_sc):
    _LOGGER.info(f"digest1: {digest1}")
    _LOGGER.info("seqcol")
    _LOGGER.info(B)
    A = scclient.retrieve(digest1, reclimit=1)
    return JSONResponse(scclient.compat_all(A, B))


def main(args=None):
    parser = build_parser()
    parser = logmuse.add_logging_options(parser)
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        print("No subcommand given")
        sys.exit(1)

    _LOGGER = logmuse.logger_via_cli(args, make_root=True)
    _LOGGER.info("Welcome to the SeqCol API app")
    _LOGGER.info(ALL_VERSIONS)

    # demo_filepath="/home/nsheff/code/seqcolapi/seqcolapi/seqcolapi_config_demo.yaml"

    print(f"args: {args}")
    if "config" in args and args.config is not None:
        scconf = create_globals(args.config, args.port)
        _LOGGER.info(f"Running on port {scconf.app['port']}")
        uvicorn.run(app, host=scconf.app["host"], port=scconf.app["port"])
    
def create_globals(config_path, port):
    """
    Create global variables for the app to use.
    """
    global scclient
    scconf = SeqColConf(filepath=config_path)
    _LOGGER.info(f"Connecting to database... {scconf.exp['database']['host']}")
    pgdb = RDBDict(
        scconf.exp["database"]["name"],
        scconf.exp["database"]["user"],
        scconf.exp["database"]["password"],
        scconf.exp["database"]["host"],
        scconf.exp["database"]["port"],
        scconf.exp["database"]["table"],
    )
    scclient = SeqColClient(
        database=pgdb, api_url_base=scconf["refget_provider_apis"], schemas=scconf["schemas"]
    )
    # You could also make a refget client here, but it's not necessary,
    # since the SeqColClient has a refget method.
    # global rgc
    # rgc = refget.RefGetClient(scconf["refget_provider_apis"], pgdb)
    seqcolapi_port = port if port else scconf.exp["server"]["port"]
    
    host = scconf.exp["server"]["host"]
    scconf.app = {"host": host, "port": seqcolapi_port}
    return scconf


if __name__ == "__main__":
    args = sys.argv
    print(args)
    main(args)
else:
    create_globals(os.environ.get("SEQCOL_CONFIG"), os.environ.get("SEQCOL_PORT"))
