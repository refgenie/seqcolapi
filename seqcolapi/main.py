import henge
import logmuse
import os
import refget
import uvicorn

from fastapi import Path, Body, FastAPI, Response
from pydantic import BaseModel, Field
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

PKG_NAME = "seqcolapi"
ALL_VERSIONS = {
    "server_version": seqcolapi_version,
    "refget_client_version": refgetclient_version,
    "python_version": python_version(),
}

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
    additional_description = (
        "For subcommand-specific options, type: '%(prog)s <subcommand> -h'"
    )
    additional_description += "\nhttps://github.com/regenie/seqcolapi"

    parser = VersionInHelpParser(
        prog=PKG_NAME, description=banner, epilog=additional_description
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {v}".format(v=seqcolapi_version),
    )

    msg_by_cmd = {"serve": "run the server"}

    subparsers = parser.add_subparsers(dest="command")

    def add_subparser(cmd, description):
        return subparsers.add_parser(cmd, description=description, help=description)

    sps = {}
    # add arguments that are common for all subparsers
    for cmd, desc in msg_by_cmd.items():
        sps[cmd] = add_subparser(cmd, desc)
        sps[cmd].add_argument(
            "-c",
            "--config",
            required=True,
            dest="config",
            help="Path to the seqcolapi config file (YAML).",
        )
        sps[cmd].add_argument(
            "-d",
            "--dbg",
            action="store_true",
            dest="debug",
            help="Set logger verbosity to debug",
        )
    # add subparser-specific arguments
    sps["serve"].add_argument(
        "-p",
        "--port",
        dest="port",
        type=int,
        help="The port the webserver should be run on.",
        default=None,
    )
    return parser


app = FastAPI(
    title="Sequence Collections API",
    description="An API providing metadata such as names, lengths, and other values for collections of reference sequences",
    version=seqcolapi_version,
)


# Models

example_digest = Path(
    ...,
    description="Sequence collection digest",
    regex=r"^\w+$",
    max_length=64,
    min_length=32,
    example="a6748aa0f6a1e165f871dbed5e54ba62",
)

example_digest_2 = Path(
    ...,
    description="Sequence collection digest",
    regex=r"^\w+$",
    max_length=64,
    min_length=32,
    example="2786eb8a921aa97018c214f64b9960a0",
)

example_digest_hg38 = Path(
    ...,
    description="Sequence collection digest",
    regex=r"^\w+$",
    max_length=64,
    min_length=32,
    example="514c871928a74885ce981faa61ccbb1a",
)

example_digest_hg38_primary = Path(
    ...,
    description="Sequence collection digest",
    regex=r"^\w+$",
    max_length=64,
    min_length=32,
    example="c345e091cce0b1df78bfc124b03fba1c",
)

example_sequence = Path(
    ...,
    description="Refget sequence digest",
    regex=r"^\w+$",
    max_length=64,
    min_length=32,
    example="76f9f3315fa4b831e93c36cd88196480",
)

example_hg38_sc = Body(
    {
        "lengths": [
            "248956422",
            "242193529",
            "198295559",
            "190214555",
            "181538259",
            "170805979",
            "159345973",
            "145138636",
            "138394717",
            "133797422",
            "135086622",
            "133275309",
            "114364328",
            "107043718",
            "101991189",
            "90338345",
            "83257441",
            "80373285",
            "58617616",
            "64444167",
            "46709983",
            "50818468",
            "16569",
            "156040895",
            "57227415",
        ],
        "names": [
            "chr1",
            "chr2",
            "chr3",
            "chr4",
            "chr5",
            "chr6",
            "chr7",
            "chr8",
            "chr9",
            "chr10",
            "chr11",
            "chr12",
            "chr13",
            "chr14",
            "chr15",
            "chr16",
            "chr17",
            "chr18",
            "chr19",
            "chr20",
            "chr21",
            "chr22",
            "chrM",
            "chrX",
            "chrY",
        ],
        "sequences": [
            "a004bc1b0bf05fc668cab6bbfd93d3eb",
            "0ccf3a67666ac53f99fcad19768f2dde",
            "bda7b228789169ae811dd8d676d517ca",
            "88a6091e2d9a609f4ea7eaef937cd4c2",
            "0f1725f15e8046a6a04e32de629b1e10",
            "08c3702d62a2c476a081d3ccd15ea30c",
            "cac9e313d08cdf40c9eeafe62b17879a",
            "9a2ebb88dc34c2af023d50219248c815",
            "41bbec590d36e711864dc6f030f0264b",
            "6b420cbb22daea77d7cc930c0a00f812",
            "0d4e0be5c4e5bc0f12912894f21a5dd8",
            "e1507ba70028a65b3f5a81b594e6f0fe",
            "7110500758388b169fe631b212b7e56c",
            "f37e77fdbacb1a0f1be5e2bf25df343d",
            "3f14ce1984dada290682eb1f564934ee",
            "88169bd58f0c5f9fd083030d1357d908",
            "0bbc162a7d963574b5989adab5651ac5",
            "388e8c7cd11a23eebf84a02d5e442bb7",
            "1c927775585df1cb09ec7c7dd1b32a6a",
            "c37960f60eff5e2cfbde87e53d262efa",
            "f0324d60ccf85288a26a47a7ca25a54a",
            "f7479d5a2a3169e2e44d97d7f2a13db1",
            "6ab1f3c8f4941e148463c40408c89e43",
            "6bdaf93397b486a58fd60b55aa2e21ca",
            "9bd609da53b41a50a724f2a0131ee9c1",
        ],
    }
)

reclimit_ex = Path(
    ...,
    description="Recursion limit, the number of times to recurse to populate digests in the structure",
    gt=-1,
    lt=2,
    example=0,
    )


STATIC_DIRNAME = "static"
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), STATIC_DIRNAME)
app.mount("/" + STATIC_DIRNAME, StaticFiles(directory=STATIC_PATH), name=STATIC_DIRNAME)
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
templates = Jinja2Templates(directory=TEMPLATES_PATH)


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
    return Response(content=rgc.refget(digest))
    # return {"message": "Hello World"}


@app.get(
    "/collection/{digest}",
    summary="Retrieve a sequence collection",
    tags=["Retrieving sequence collections"],
)
async def collection(digest: str=example_digest):
    try:
        # res = sc.retrieve(digest)
        # print(res)
        return JSONResponse(content=sc.retrieve(digest, reclimit=1))
    except:
        return {}
    # return {"message": "Hello World"}


@app.get(
    "/collection/{digest}/{reclimit}",
    summary="Retrieve a sequence collection",
    tags=["Retrieving sequence collections"],
)
async def collection_recursive(digest: str=example_digest, reclimit: int=reclimit_ex):

    if reclimit > 1:
        return Response(
            content="Error: recursion > 1 disabled. Use the /refget server to retrieve sequences."
        )
    try:
        # res = sc.retrieve(digest, reclimit=reclimit)
        # print(res)
        return JSONResponse(content=sc.retrieve(digest, reclimit=reclimit))
    except:
        return {}
    # return {"message": "Hello World"}


@app.get(
    "/comparison/{digest1}/{digest2}",
    summary="Compare two sequence collections hosted on the server",
    tags=["Comparing sequence collections"],
)
async def compare2digests(
    digest1: str = example_digest_hg38, digest2: str = example_digest_hg38_primary
):
    _LOGGER.info("Compare called")
    return JSONResponse(sc.compare_digests(digest1, digest2))


@app.post(
    "/comparison/{digest1}",
    summary="Compare a local sequence collection to one on the server",
    tags=["Comparing sequence collections"],
)
async def compare1digest(digest1: str = example_digest_hg38, B: dict = example_hg38_sc):
    # inputA = comparison["seqcolA"]
    # inputB = comparison["seqcolB"]
    # if isinstance(inputA, str):
    # scA = sc.retrieve(inputA)
    # elif isinstance(inputA, dict):
    # scA = inputA

    _LOGGER.info("digest1: " + digest1)
    _LOGGER.info("seqcol")
    _LOGGER.info(B)
    A = sc.retrieve(digest1, reclimit=1)
    return JSONResponse(sc.compat_all(A, B))


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
    pgdb = RDBDict(
        scc.database.name,
        scc.database.user,
        scc.database.password,
        scc.database.host,
        scc.database.port,
    )

    rgc = refget.RefGetClient(scc.refget_provider_apis, pgdb)

    sc = SeqColClient(
        database=pgdb, api_url_base=scc.refget_provider_apis, schemas=scc.schemas
    )
    seqcolapi_port = args.port if args.port else scc.server.port
    _LOGGER.info("Running on port {}".format(seqcolapi_port))
    uvicorn.run(app, host=scc.server.host, port=seqcolapi_port)
