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
]

api_root = "http://0.0.0.0:8100"
demo_root = "/home/nsheff/code/refget/demo_fasta"
demo_file = "demo0.fa"
response_file = "tests/demo0_collection.json"
import refget

def check_response(demo_file, response_file):
    digest = refget.fasta_file_to_digest(f"{demo_root}/{demo_file}")
    res = requests.get(f"{api_root}/collection/{digest}")
    server_answer = json.loads(res.content)
    with open(response_file) as fp:
        correct_answer = json.load(fp)
    assert server_answer == correct_answer, "Collection endpoint failed"

def test_api():
    check_response(*COLLECTION_TESTS[0])
