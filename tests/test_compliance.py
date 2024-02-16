# Draft of a compliance suite for the API

import json
import requests

# Collection endpoints
DEMO_FILES = [
    "demo0.fa",
    "demo1.fa.gz",
    "demo2.fa",
    "demo3.fa",
    "demo4.fa",
    "demo5.fa.gz",
    "demo6.fa",
]

COLLECTION_TESTS = [
    (DEMO_FILES[0], "tests/demo0_collection.json"),
    (DEMO_FILES[1], "tests/demo1_collection.json"),
]

# This is optional, so we could turn off for a compliance test
TEST_SORTED_NAME_LENGTH_PAIRS = True

api_root = "http://0.0.0.0:8100"
demo_root = "/home/nsheff/code/refget/demo_fasta"
demo_file = "demo0.fa"
response_file = "tests/demo0_collection.json"
import refget


def check_server_is_running():
    res = requests.get(f"{api_root}/ping")
    assert res.status_code == 200, "Server is not running"


def read_url(url):
    import yaml

    print("Reading URL: {}".format(url))
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        response = urlopen(url)
    except HTTPError as e:
        raise e
    data = response.read()  # a `bytes` object
    text = data.decode("utf-8")
    print(text)
    return yaml.safe_load(text)


def check_response(demo_file, response_file):

    # Need schema to make sure we eliminate inherent attributes correctly
    schema_path = "https://schema.databio.org/refget/SeqColArraySetInherent.yaml"

    schema = read_url(schema_path)

    digest = refget.fasta_file_to_digest(f"{demo_root}/{demo_file}", schema=schema)
    print(f"Digest: {digest}")
    res = requests.get(f"{api_root}/collection/{digest}")
    server_answer = json.loads(res.content)
    with open(response_file) as fp:
        correct_answer = json.load(fp)

    assert (
        server_answer["sequences"] == correct_answer["sequences"]
    ), "Collection endpoint failed: sequence mismatch"
    assert (
        server_answer["names"] == correct_answer["names"]
    ), "Collection endpoint failed"
    assert (
        server_answer["lengths"] == correct_answer["lengths"]
    ), "Collection endpoint failed"
    if TEST_SORTED_NAME_LENGTH_PAIRS:
        assert (
            server_answer["sorted_name_length_pairs"]
            == correct_answer["sorted_name_length_pairs"]
        ), "Collection endpoint failed"


class TestAPI:

    def test_collection_endpoint(self):
        check_response(*COLLECTION_TESTS[0])
        check_response(*COLLECTION_TESTS[1])
