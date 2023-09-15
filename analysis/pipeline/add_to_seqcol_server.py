"""
A script I wrote to be compatible with looper to run a single 
fasta file through the seqcol digest computation and then add
to the server.
"""
import sys
import yacman
import seqcol
import henge

sys.path.append("../seqcolapi")
from scconf import RDBDict
pgdb = RDBDict()  # parameterized through env vars

scc = seqcol.SeqColConf()
schenge = seqcol.SeqColHenge(
    database=pgdb,
    schemas=["/home/nsheff/code/seqcol/seqcol/schemas/SeqColArraySetInherent.yaml"],
    checksum_function=henge.sha512t24u_digest)

print(f"SeqColHenge: {schenge}")

sample_config = sys.argv[1]  # get first command-line argument, sample config file
print(f"Sample config: {sample_config}")

sample = yacman.YAMLConfigManager(filepath=sample_config)
print(f"Sample: {sample}")

print("Loading fasta...")
result = schenge.load_fasta_from_filepath(sample["fasta"])
print(f"Writing digest to config")
with sample_config as cfg:
    cfg[i]["seqcol_digest"] = result["digest"]
    cfg.write()

