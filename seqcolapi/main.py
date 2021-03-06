import henge
import logmuse
import os
import refget
import uvicorn

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from platform import python_version
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from ubiquerg import VersionInHelpParser
from yacman import get_first_env_var


from .scconf import RDBDict, SeqColConf
from ._version import __version__ as seqcolapi_version
from refget._version import __version__ as refgetclient_version

PKG_NAME="seqcolapi"
ALL_VERSIONS = {"server_version": seqcolapi_version, 
    "refget_client_version": refgetclient_version, 
    "python_version": python_version()}

# We don't need the full SeqColClient, 
# which also has loading capability, and requires pyfaidx, which requires
# biopython, which requires numpy, which is huge and can't compile the in
# default fastapi container.
# but switching from alpine to slim allows install of numpy;
# This inflates the container size from 262Mb to 350Mb; perhaps that's worth paying.
# class SeqColClient(refget.RefGetClient):
#     def retrieve(self, druid, reclimit=None, raw=False):
#         try:
#             return super(SeqColClient, self).retrieve(druid, reclimit, raw)
#         except henge.NotFoundException as e:
#             _LOGGER.debug(e)
#             try:
#                 return self.refget(druid)
#             except Exception as e:
#                 _LOGGER.debug(e)
#                 raise e
#                 return henge.NotFoundException("{} not found in database, or in refget.".format(druid))

from seqcol import SeqColClient

def build_parser():
    """
    Building argument parser

    :return argparse.ArgumentParser
    """
    banner = "%(prog)s - API for sequence collections"
    additional_description = "For subcommand-specific options, type: '%(prog)s <subcommand> -h'"
    additional_description += "\nhttps://github.com/regenie/seqcolapi"

    parser = VersionInHelpParser(
        prog=PKG_NAME,
        description=banner,
        epilog=additional_description)

    parser.add_argument(
        "-V", "--version",
        action="version",
        version="%(prog)s {v}".format(v=seqcolapi_version))

    msg_by_cmd = {
        "serve": "run the server"}

    subparsers = parser.add_subparsers(dest="command")

    def add_subparser(cmd, description):
        return subparsers.add_parser(
            cmd, description=description, help=description)

    sps = {}
    # add arguments that are common for all subparsers
    for cmd, desc in msg_by_cmd.items():
        sps[cmd] = add_subparser(cmd, desc)
        sps[cmd].add_argument(
            '-c', '--config', required=True, dest="config",
            help="Path to the seqcolapi config file (YAML).")
        sps[cmd].add_argument(
            "-d", "--dbg",
            action="store_true",
            dest="debug",
            help="Set logger verbosity to debug")
    # add subparser-specific arguments
    sps["serve"].add_argument(
        "-p", "--port",
        dest="port",
        type=int,
        help="The port the webserver should be run on.", default=None)
    return parser


app = FastAPI(title="SeqColAPI",
    description="An API for Sequence Collections",
    version=seqcolapi_version)


STATIC_DIRNAME = "static"
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), STATIC_DIRNAME)
app.mount("/" + STATIC_DIRNAME, StaticFiles(directory=STATIC_PATH), name=STATIC_DIRNAME)
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
templates = Jinja2Templates(directory=TEMPLATES_PATH)



@app.get("/test")
async def root():
    return Response(content="Welcome to the test seqcol server.")

@app.get("/")
@app.get("/index")
async def index(request: Request):
    """
    Returns a landing page HTML with the server resources ready do download. No inputs required.
    """
    templ_vars = {"request": request, 
                  "openapi_version": app.openapi()["openapi"]}
    _LOGGER.debug("merged vars: {}".format(dict(templ_vars, **ALL_VERSIONS)))
    return templates.TemplateResponse("index.html", dict(templ_vars, **ALL_VERSIONS))



@app.get("/refget/{digest}")
async def root(digest: str):
    return Response(content=rgc.refget(digest))
    # return {"message": "Hello World"}

@app.get("/seqcol/{digest}")
async def root(digest: str):
    try:
        # res = sc.retrieve(digest)
        # print(res)
        return JSONResponse(content=sc.retrieve(digest))
    except:
        return {}
    # return {"message": "Hello World"}

@app.get("/seqcol/{digest}/{reclimit}")
async def root(digest: str, reclimit: int):

    if reclimit > 1:
        return Response(content="Error: recursion > 1 disabled. Use the /refget server to retrieve sequences.")
    try:
        # res = sc.retrieve(digest, reclimit=reclimit)
        # print(res)
        return JSONResponse(content=sc.retrieve(digest, reclimit=reclimit))
    except:
        return {}
    # return {"message": "Hello World"}

def main():
    global sc
    global rgc
    global _LOGGER
    parser = build_parser()
    parser = logmuse.add_logging_options(parser)
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        print("No subcommand given")
        sys.exit(1)

    _LOGGER = logmuse.logger_via_cli(args, make_root=True)
    _LOGGER.info("Welcome to the SeqCol API app")

    # demo_filepath="/home/nsheff/code/seqcolapi/seqcolapi/seqcolapi_config_demo.yaml"
    scc = SeqColConf(filepath=args.config)
    _LOGGER.info(f"Connecting to database... {scc.database.host}")
    pgdb = RDBDict(scc.database.name,
                    scc.database.user,
                    scc.database.password,
                    scc.database.host,
                    scc.database.port)

    rgc = refget.RefGetClient(scc.refget_provider_apis, pgdb)

    sc = SeqColClient(database=pgdb,
        api_url_base=scc.refget_provider_apis,
        schemas=scc.schemas)
    seqcolapi_port = args.port if args.port else scc.server.port
    _LOGGER.info("Running on port {}".format(seqcolapi_port))
    uvicorn.run(app, host=scc.server.host,
            port=seqcolapi_port)
