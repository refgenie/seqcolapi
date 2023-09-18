import hashlib
import os
import requests

from tqdm import tqdm
from pathlib import Path

def compute_file_md5(file_name: str) -> str:
    hash_md5 = hashlib.md5()
    hash_md5.update(open(file_name, "rb").read())
    return hash_md5.hexdigest()

def download(url: str, file_path: str, chunk_size: int = 1024) -> None:
    """Download a file from a URL to a local file path."""
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    Path(os.path.dirname(file_path)).mkdir(parents=True, exist_ok=True)

    with open(file_path, "wb") as f, tqdm(
        desc=file_path,
        total=total_size,
        unit="iMB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                size = f.write(chunk)
                bar.update(size)
    return


def get_content(url: str) -> str:
    r = requests.get(url)
    return r.content


def add_attributes_for_ensembl_genomes(g: dict, data_path: str) -> dict:
    g["file_name"] = f"Homo_sapiens-{g['assembly_accession']}-unmasked.fa.gz"
    g["url"] = f"{g['ftp_dumps']}/ensembl/genome/{g['file_name']}"
    g["local_file"] = f'{data_path}/{g["assembly"]}.unmasked.fa.gz'
    md5s = get_content(f'{g["ftp_dumps"]}/ensembl/genome/md5sum.txt')
    d = {}  # extract the md5s from text file
    for v, k in [line.split() for line in md5s.strip().decode().split("\n")]:
        d[k] = v
    g["remote_md5"] = d[g["file_name"]]  # add correct md5 to dict

    return g


def download_and_cache(url: str, local_file: str, correct_md5: str) -> None:
    if os.path.exists(local_file):  # if the file exists, don't download
        print(f"{local_file} exists, checking md5...")
        local_md5 = compute_file_md5(local_file)
        if local_md5 == correct_md5:
            print(f"Checkums match, skipping: {local_md5}")
            return
        else:
            print(
                "Checksum mismatch! Local: '{local_md5}'; expected: '{correct_md5}' Removing local file."
            )
            os.remove(local_file)
    download(url, local_file)
