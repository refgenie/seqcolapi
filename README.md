# seqcolapi

Alpha version of a sequence collections server

## Instructions

Install natively with `pip install .`

Run natively:
```
export POSTGRES_PASSWORD=`pass aws/rds_postgres`
seqcolapi serve -c /home/nsheff/code/seqcol.databio.org/config/seqcolapi.yaml
```

To build the docker file:

```
docker build --no-cache -t scim .
```

To run in a container:

```
export POSTGRES_PASSWORD=`pass aws/rds_postgres` 
docker run --rm -p 8000:8000 --name sccon \
  --env "POSTGRES_PASSWORD" \
  --volume $CODE/seqcolapi.databio.org/config/seqcolapi.yaml:/config.yaml \
  scim seqcolapi serve -c /config.yaml
```

Left to do:
- [x] it already retrieves from a refget server.
- [x] let me insert stuff using only checksums.
- [ ] make it take 2 refget servers correctly.
