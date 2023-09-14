import henge
import json
import logging
import logmuse
import os
import refget
import uvicorn
import sys

from fastapi import Body, FastAPI, Response
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from typing import Union

from .cli import build_parser
from .const import *
from .scconf import RDBDict, SeqColConf
from .examples import *

from seqcol import SeqColHenge, format_itemwise

global _LOGGER

_LOGGER = logging.getLogger(__name__)
# _LOGGER.setLevel(logging.DEBUG)

templates = Jinja2Templates(directory=TEMPLATES_PATH)

_LOGGER.info(ALL_VERSIONS)

app = FastAPI(
    title="Sequence Collections API",
    description="An API providing metadata such as names, lengths, and other values for collections of reference sequences",
    version=seqcolapi_version,
)

origins = ["*"]

app.add_middleware(  # This is a public API, so we allow all origins
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/" + STATIC_DIRNAME, StaticFiles(directory=STATIC_PATH), name=STATIC_DIRNAME)


@app.get("/", summary="Home page", tags=["General endpoints"])
async def index(request: Request):
    """
    Returns a landing page HTML with the server resources ready to download. No inputs required.
    """
    templ_vars = {"request": request, "openapi_version": app.openapi()["openapi"]}
    _LOGGER.debug("merged vars: {}".format(dict(templ_vars, **ALL_VERSIONS)))
    return templates.TemplateResponse("index.html", dict(templ_vars, **ALL_VERSIONS))


@app.get("/service-info", summary="GA4GH service info", tags=["General endpoints"])
async def service_info():
    ret = {
        "id": "org.databio.seqcolapi",
        "name": "Sequence collections",
        "type": {
            "group": "org.ga4gh",
            "artifact": "seqcol",
            "version": ALL_VERSIONS["seqcol_spec_version"],
        },
        "description": "An API providing metadata such as names, lengths, and other values for collections of reference sequences",
        "organization": {"name": "Databio Lab", "url": "https://databio.org"},
        "contactUrl": "https://github.com/refgenie/seqcol/issues",
        "documentationUrl": "https://seqcolapi.databio.org",
        "updatedAt": "2021-03-01T00:00:00Z",
        "environment": "dev",
        "version": ALL_VERSIONS["seqcolapi_version"],
        "seqcol": {"schema": scclient.schemas, "sorted_name_length_pairs": True},
    }
    return JSONResponse(content=ret)


@app.get(
    "/sequence/{digest}",
    summary="Retrieve raw sequence via refget protocol",
    tags=["General endpoints"],
)
async def refget(digest: str = example_sequence):
    return Response(content=scclient.refget(digest))


@app.get(
    "/collection/{digest}",
    summary="Retrieve a sequence collection",
    tags=["Retrieving sequence collections"],
)
async def collection_recursive(
    digest: str = example_digest,
    level: Union[int, None] = None,
    format: Union[str, None] = None,
):
    print("retriving collection")
    if level == None:
        level = 2
    if level > 2:
        raise HTTPException(
            status_code=400,
            detail="Error: recursion > 1 disabled. Use the /refget server to retrieve sequences.",
        )
    csc = scclient.retrieve(digest, reclimit=level - 1)
    try:
        if format == "collated":
            if len(csc["lengths"]) > 10000:
                raise HTTPException(
                    status_code=413,
                    detail="This server won't collate collections with > 10000 sequences",
                )
            return JSONResponse(content=format_itemwise(csc))
        else:
            return JSONResponse(content=csc)
    except:
        return {}


@app.get(
    "/comparison/{digest1}/{digest2}",
    summary="Compare two sequence collections hosted on the server",
    tags=["Comparing sequence collections"],
)
async def compare_2_digests(
    digest1: str = example_digest_hg38, digest2: str = example_digest_hg38_primary
):
    _LOGGER.info("Compare called")
    result = {}
    result["digests"] = {"a": digest1, "b": digest2}
    result.update(scclient.compare_digests(digest1, digest2))
    return JSONResponse(result)


@app.post(
    "/comparison/{digest1}",
    summary="Compare a local sequence collection to one on the server",
    tags=["Comparing sequence collections"],
)
async def compare_1_digest(
    digest1: str = example_digest_hg38, B: dict = example_hg38_sc
):
    _LOGGER.info(f"digest1: {digest1}")
    _LOGGER.info("seqcol")
    _LOGGER.info(B)
    A = scclient.retrieve(digest1, reclimit=1)
    return JSONResponse(scclient.compat_all(A, B))


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
    scclient = SeqColHenge(
        database=pgdb,
        api_url_base=scconf["refget_provider_apis"],
        schemas=scconf["schemas"],
    )
    seqcolapi_port = port if port else scconf.exp["server"]["port"]
    host = scconf.exp["server"]["host"]
    scconf.app = {"host": host, "port": seqcolapi_port}
    return scconf


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

    print(f"args: {args}")
    if "config" in args and args.config is not None:
        scconf = create_globals(args.config, args.port)
        _LOGGER.info(f"Running on port {scconf.app['port']}")
        uvicorn.run(app, host=scconf.app["host"], port=scconf.app["port"])


if __name__ != "__main__":
    if os.environ.get("SEQCOL_CONFIG"):
        # Establish global config when running through uvicorn CLI
        create_globals(os.environ.get("SEQCOL_CONFIG"), os.environ.get("SEQCOL_PORT"))
