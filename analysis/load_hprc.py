import yacman
from utilities import *

from tqdm import tqdm

# Data from https://projects.ensembl.org/hprc/
yaml_genomes_path = "config/hprc.yaml"
# genomes = load_yaml(yaml_genomes_path)
# with open(yaml_genomes_path, "r") as f:
#     ensembl_genomes = yaml.safe_load(f)

ensembl_genomes = yacman.YAMLConfigManager(filepath=yaml_genomes_path)

for i, g in enumerate(tqdm(ensembl_genomes)):
    print(f"Pre-processing {g['assembly']}...")
    if ensembl_genomes[i].get("fasta") is not None:
        print("Already downloaded")
        continue
    g = add_attributes_for_ensembl_genomes(g)
    download_and_cache(g["url"], g["local_file"], g["remote_md5"])
    g["fasta"] = g["local_file"]
    ensembl_genomes[i] = g
    with ensembl_genomes as cfg:
        cfg.write()


# TODO: these pangenome elements should be run through refgenie...

pgdb = scconf.RDBDict()  # parameterized through env vars


