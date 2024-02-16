# Analysis

This is a looper project to add HPRC genomes to the seqcol server

## Prerequisites

1. Install the `checksumseq` command by installing [rust-gc-count](https://crates.io/crates/rust-gc-count).

```
cargo install rust-gc-count
```

2. Put `.fastq.gz` files into the `/data` folder.

## Compute digests for individual sequences using rust binary



```
./calc_checksum.sh
```

## Load into seqcol server and compute final digests

There's a pipeline in `pipeline/add_to_seqcol_server.py` that takes a fasta file and adds it to the server.

And,

```
cd analysis
source ../servers/seqcolapi.databio.org/production.env
# looper run --limit 1 --package local  # for testing
looper run --package local
```



# How to load sequence collections into the server

1. Make a PEP with the FASTA files you want to process.
2. Run looper on it.

```
source servers/seqcolapi.databio.org/production.env
# looper run --limit 1 --package local  # for testing
looper run --package local config/demo_fasta.csv --limit 1