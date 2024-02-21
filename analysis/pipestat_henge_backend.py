import sys
sys.path.append("../../seqcolapi")

from scconf import RDBDict

import pipestat

psm = pipestat.PipestatManager(
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

# If I wrap it so the getters/setters will get `["value"]` then I think it will work.
class MyPipestatDict(pipestat.PipestatManager):
    def __getitem__(self, key):
        return super().__getitem__(key)["value"]
    def __setitem__(self, key, value):
        super().__setitem__(key, {"value": value})


psm2 = MyPipestatDict(
    record_identifier="sample1",
    results_file_path="analysis/temp.yaml",
    schema_path="analysis/seqcol_pipestat_schema.yaml",
)
psm2["sample2"]
psm2["sample5"] = "lookie!"
psm2["sample5"]

# TODO: build a henge using this thing.



