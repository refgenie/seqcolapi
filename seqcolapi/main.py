import henge
import json
import logging
import logmuse
import os
import sys
import uvicorn
import yacman

from fastapi import Body, FastAPI, Response
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse, FileResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from typing import Union

from .cli import build_parser
from .const import *
from .scconf import RDBDict
from .examples import *

from refget import SeqColConf, SeqColHenge, format_itemwise

global _LOGGER

_LOGGER = logging.getLogger(__name__)

templates = Jinja2Templates(directory=TEMPLATES_PATH)

for key, value in ALL_VERSIONS.items():
    _LOGGER.info(f"{key}: {value}")

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

@app.get('favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(f"/static/favicon.ico")


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
            "artifact": "refget.seqcol",
            "version": ALL_VERSIONS["seqcol_spec_version"],
        },
        "description": "An API providing metadata such as names, lengths, and other values for collections of reference sequences",
        "organization": {"name": "Databio Lab", "url": "https://databio.org"},
        "contactUrl": "https://github.com/refgenie/seqcol/issues",
        "documentationUrl": "https://seqcolapi.databio.org",
        "updatedAt": "2021-03-01T00:00:00Z",
        "environment": "dev",
        "version": ALL_VERSIONS["seqcolapi_version"],
        "seqcol": {"schema": schenge.schemas, "sorted_name_length_pairs": True},
    }
    return JSONResponse(content=ret)


@app.get(
    "/sequence/{digest}",
    summary="Retrieve raw sequence via refget protocol",
    tags=["Refget endpoints"],
)
async def refget(digest: str = example_sequence):
    return Response(content=schenge.refget(digest))


@app.get(
    "/collection/{digest}",
    summary="Retrieve a sequence collection",
    tags=["Retrieving sequence collections"],
)
async def collection(
    digest: str = example_digest, level: Union[int, None] = None, collated: bool = True
):
    print("Retrieving collection")
    if level == None:
        level = 2
    if level > 2:
        raise HTTPException(
            status_code=400,
            detail="Error: recursion > 1 disabled. Use the /refget server to retrieve sequences.",
        )
    try:
        csc = schenge.retrieve(digest, reclimit=level - 1)
    except henge.NotFoundException as e:
        _LOGGER.debug(e)
        raise HTTPException(
            status_code=404,
            detail="Error: collection not found. Check the digest and try again.",
        )
    try:
        if not collated:
            if len(csc["lengths"]) > 10000:
                raise HTTPException(
                    status_code=413,
                    detail="This server won't decollate collections with > 10000 sequences",
                )
            else:
                return JSONResponse(content=format_itemwise(csc))
        else:
            return JSONResponse(content=csc)
    except:
        raise HTTPException(
            status_code=404,
            detail="Error: collection not found. Check the digest and try again.",
        )


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
    try:
        result.update(schenge.compare_digests(digest1, digest2))
    except henge.NotFoundException as e:
        _LOGGER.debug(e)
        raise HTTPException(
            status_code=404,
            detail="Error: collection not found. Check the digest and try again.",
        )
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
    _LOGGER.info(f"B: {B}")
    A = schenge.retrieve(digest1, reclimit=1)
    return JSONResponse(schenge.compat_all(A, B))


@app.get(
    "/list-by-offset",
    summary="List sequence collections on the server",
    tags=["Listing sequence collections"],
)
async def list_collections_by_offset(limit: int = 100, offset: int = 0):
    return JSONResponse(schenge.list_by_offset(limit=limit, offset=offset))

@app.get(
    "/list",
    summary="List sequence collections on the server",
    tags=["Listing sequence collections"],
)
async def list_collections_by_token(page_size: int = 100, cursor: str = None):
    return JSONResponse(schenge.list(page_size=page_size, cursor=cursor))


# Mount statics after other routes for lower precedence
app.mount(f"/" , StaticFiles(directory=STATIC_PATH), name=STATIC_DIRNAME)

def create_globals(scconf: yacman.YAMLConfigManager):
    """
    Create global variables for the app to use.
    """
    _LOGGER.info(f"Connecting to database... {scconf.exp['database']['host']}")
    global schenge
    pgdb = RDBDict(
        db_name=scconf.exp["database"]["name"],
        db_user=scconf.exp["database"]["user"],
        db_password=scconf.exp["database"]["password"],
        db_host=scconf.exp["database"]["host"],
        db_port=scconf.exp["database"]["port"],
        db_table=scconf.exp["database"]["table"],
        )
    _LOGGER.info(f"Using schema: {scconf['schemas']}")
    schenge = SeqColHenge(
        database=pgdb,
        schemas=scconf["schemas"],
    )
    return scconf


def main(injected_args=None):
    # Entry point for running from console_scripts, installed package
    parser = build_parser()
    parser = logmuse.add_logging_options(parser)
    args = parser.parse_args()
    if injected_args:
        args.__dict__.update(injected_args)
    if not args.command:
        parser.print_help()
        print("No subcommand given")
        sys.exit(1)

    _LOGGER = logmuse.logger_via_cli(args, make_root=True)
    _LOGGER.info(f"args: {args}")
    if "config" in args and args.config is not None:
        scconf = SeqColConf(filepath=args.config)
        create_globals(scconf)
        port = args.port or scconf.exp["server"]["port"]
        _LOGGER.info(f"Running on port {port}")
        uvicorn.run(app,
                    host=scconf.exp["server"]["host"], 
                    port=port)
    else:
        _LOGGER.error("Configure by passing -c SEQCOLAPI_CONFIG ")

if __name__ != "__main__":
    # Entrypoint for running through uvicorn CLI (dev)
    if os.environ.get("SEQCOLAPI_CONFIG") is not None:
        scconf = SeqColConf()
        create_globals(scconf)
    else:
        _LOGGER.error("Configure by setting SEQCOLAPI_CONFIG env var")
