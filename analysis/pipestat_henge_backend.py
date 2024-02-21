import henge
import logging
import pipestat
import refget
import sys

sys.path.append("../../seqcolapi")
from scconf import RDBDict

# If I wrap it so the getters/setters will get `["value"]` then I think it will work.
class MyPipestatDict(pipestat.PipestatManager):
    def __getitem__(self, key):
        return super().__getitem__(key)["value"]
    def __setitem__(self, key, value):
        super().__setitem__(key, {"value": value})


# psm = pipestat.PipestatManager(
#     record_identifier="sample1",
#     results_file_path="analysis/temp.yaml",
#     schema_path="analysis/seqcol_pipestat_schema.yaml",
# )

_LOGGER = logging.getLogger()  # root logger
stream = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(levelname)s %(asctime)s | %(name)s:%(module)s:%(lineno)d > %(message)s ")
stream.setFormatter(fmt)
_LOGGER.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
_LOGGER.addHandler(stream)
_LOGGER2 = logging.getLogger("henge")
_LOGGER2.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))


psm2 = MyPipestatDict(
    record_identifier="sample1",
    results_file_path="analysis/temp.yaml",
    schema_path="analysis/seqcol_pipestat_schema.yaml",
)


psm.pipeline_name  # taken from schema file
psm.record_identifier

psm.retrieve_one(record_identifier="sample1")

psm.data
psm.result_schemas

psm.report({"value": "abcdefg"})
psm.retrieve_one("value")

psm.retrieve_one("sample1", "value")

psm["sample2"] = {"value": "hijklmn"}

psm["sample2"]

psm.report({"value": "arg"}, record_identifier="sample2")

psm["sample5"] = "content_goes_here"




psm2["sample2"]
psm2["sample5"] = "new value!!"
psm2["sample5"]

# TODO: build a henge using this thing.
scc = refget.SeqColConf()

schenge = refget.SeqColHenge(
    database=psm2,
    schemas=["/home/nsheff/code/refget/refget/schemas/SeqColArraySetInherent.yaml"],
    checksum_function=henge.sha512t24u_digest)

schenge
schenge.list()
schenge.load_fasta_from_filepath("analysis/data/test_data/base.fa")
schenge.henges
psm2.retrieve_one("fLf5M0BOIPIqcfbE6R8oYwxsy-PnoV32_item_type")


# Second idea: 
# Just use pipestat, with the schema from the seqcol, instead of using a henge.
# How would this work?
# Given a seqcol, just compute its identifier, then stick the whole thing into pipestat as an object
# Then, when you want to retrieve it, you can just retrieve the whole thing and use it as a seqcol.




# Demo for bug in pipestat dealing with samples with common prefix:

psm3 = pipestat.PipestatManager(
    record_identifier="sample1",
    results_file_path="analysis/bug_test.yaml",
    schema_path="analysis/seqcol_pipestat_schema.yaml",
)

psm3.report({"value": "abcdefg"}, record_identifier="sample1")
psm3.report({"value": "12345"}, record_identifier="sample")
psm3.retrieve_one("sample", "value")

psm3.retrieve_one("sample1", "value")


psm3.report({"value": "This is a new value"}, record_identifier="sample1", force_overwrite=True)
psm3.retrieve_one("sample1", "value")
