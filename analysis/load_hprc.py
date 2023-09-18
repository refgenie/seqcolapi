import logging
import sys
import yacman

from tqdm import tqdm

# Locals
sys.path.append("analysis")
from utilities import *


# Data from https://projects.ensembl.org/hprc/
yaml_genomes_path = "analysis/config/hprc.yaml"
# genomes = load_yaml(yaml_genomes_path)
# with open(yaml_genomes_path, "r") as f:
#     ensembl_genomes = yaml.safe_load(f)

ensembl_genomes = yacman.YAMLConfigManager(filepath=yaml_genomes_path)

for i, g in enumerate(tqdm(ensembl_genomes)):
    print(f"Pre-processing {g['assembly']}...")
    if ensembl_genomes[i].get("fasta") is not None:
        print("Already downloaded")
        continue
    g = add_attributes_for_ensembl_genomes(g, data_path="analysis/data")
    download_and_cache(g["url"], g["local_file"], g["remote_md5"])
    g["fasta"] = g["local_file"]
    ensembl_genomes[i] = g
    with ensembl_genomes as cfg:
        cfg.write()


# TODO: these pangenome elements should be run through refgenie...

sys.path.append("seqcolapi")
from scconf import RDBDict
pgdb = RDBDict()  # parameterized through env vars

import seqcol
scc = seqcol.SeqColConf()
import henge
schenge = seqcol.SeqColHenge(
    database=pgdb,
    schemas=["/home/nsheff/code/seqcol/seqcol/schemas/SeqColArraySetInherent.yaml"],
    checksum_function=henge.sha512t24u_digest)


# set logging
_LOGGER = logging.getLogger()  # root logger
stream = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(levelname)s %(asctime)s | %(name)s:%(module)s:%(lineno)d > %(message)s ")
stream.setFormatter(fmt)
_LOGGER.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
_LOGGER.addHandler(stream)

seqcol.fasta_file_to_seqcol(ensembl_genomes[1]["fasta"])


# results = schenge.load_multiple_fastas(demo_fasta_files)
# TODO: Remove fasta processing from seqcol; rely on Andy's rust utility instead
# it's way faster.
for i, g in enumerate(tqdm(ensembl_genomes)):
    _LOGGER.info(f"Pre-processing i={i}: {g['assembly']}...")
    result = schenge.load_fasta_from_filepath(g["fasta"])  # here
    with ensembl_genomes as cfg:
        cfg[i]["seqcol_digest"] = result["digest"]
        cfg.write()
