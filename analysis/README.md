# Analysis

## Compute digests for individual sequences using rust binary

```
./calc_checksum.sh
```

## Load into seqcol server and compute final digests

And,

```
cd analysis
source ../servers/seqcolapi.databio.org/production.env
# looper run --limit 1 --package local  # for testing
looper run --package local
```

