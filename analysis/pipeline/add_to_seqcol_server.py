"""
A script I wrote to be compatible with looper to run a single 
fasta file through the seqcol digest computation and then add
to the server.
"""
import os
import sys
import yacman
import seqcol
import henge

sample_config = sys.argv[1]  # get first command-line argument, sample config file
print(f"Sample config: {sample_config}")

sample = yacman.YAMLConfigManager(filepath=sample_config)
print(f"Sample: {sample}")

pconfig = yacman.YAMLConfigManager(filepath="config/hprc.yaml")

# if "seqcol_digest" in pconfig[sample_config["sample_name"]]:
#     print("Sample already has seqcol_digest")
#     sys.exit(0)

import logging
_LOGGER = logging.getLogger()  # root logger
stream = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(levelname)s %(asctime)s | %(name)s:%(module)s:%(lineno)d > %(message)s ")
stream.setFormatter(fmt)
_LOGGER.setLevel(os.environ.get("LOGLEVEL", "INFO"))
_LOGGER.addHandler(stream)


import pipestat
psm = pipestat.PipestatManager(
    sample_name=sample["sample_name"],
    schema_path="pipeline/output_schema.yaml",
    results_file_path="results.yaml",
    pipeline_type="sample"
)


sys.path.append("../seqcolapi")
from scconf import RDBDict
pgdb = RDBDict()  # parameterized through env vars

scc = seqcol.SeqColConf()
schenge = seqcol.SeqColHenge(
    database=pgdb,
    schemas=["/home/nsheff/code/seqcol/seqcol/schemas/SeqColArraySetInherent.yaml"],
    checksum_function=henge.sha512t24u_digest)

print(f"SeqColHenge: {schenge}")

# Don't do it this way, it's slow.
# print("Loading fasta...")
# result = schenge.load_fasta_from_filepath(sample["fasta"])

print("Loading from chromsizes...")
result = schenge.load_from_chromsizes(sample["fasta"] + ".checksums")

# I once thought about just writing it back to the config file, but...
# there *is* no config file that works like this since I'm using pephub.
# print(f"Writing digest to config")
# with pconfig as cfg:
#     cfg[sample["sample_name"]]["seqcol_digest"] = result["digest"]
#     cfg.write()

psm.report({"seqcol_digest": result["digest"]}, sample_name=sample["sample_name"])

