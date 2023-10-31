# seqcolapi

This repository contains:

1. Beta version of sequence collections server software, the `seqcolapi` package. This package is based on the `seqcol` package. It simply provides an API wrapper, implementing the seqcol service.
2. Configuration and GitHub Actions for demo server instance ([seqcolapi.databio.org subfolder](/seqcolapi.databio.org)).

## Instructions

### Running with docker

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
  scim seqcolapi serve -c /config.yaml -p 8000
```

To deploy container to dockerhub:

Use github action in this repo which deploys on release, or through manual dispatch.


Left to do:
- [x] it already retrieves from a refget server.
- [x] let me insert stuff using only checksums.
- [ ] make it take 2 refget servers correctly.


## seqcolapi.databio.org

Config file located in /config.

This will use the image in docker.io://databio/seqcolapi, github repo: [refgenie/seqcolapi](https://github.com/refgenie/seqcolapi) as base, bundle it with the above config, and deploy to the shefflab ECS.


To load up new data:
```
cd analysis
source ../servers/localhost/dev_local.env
ipython3
```

Now run `load_fasta.py`

## Deploy to AWS ECS

### Testing locally first

Build the seqcolapi image

```
cd
docker build -t docker.io/databio/seqcolapi:latest .
```

```
docker pull docker.io/databio/seqcolapi:latest
cd servers/seqcolapi.databio.org
docker build -t scim .
docker run \
  -e POSTGRES_HOST=$POSTGRES_HOST \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  --network=host \
  scim
```

To upgrade the software:

1. Ensure the [seqcol](https://github.com/refgenie/seqcol/) package master branch is as you want it.
2. Deploy the updated [secqolapi](https://github.com/refgenie/seqcolapi/) app to dockerhub (using manual dispatch, or deploy on github release).
3. Finally, deploy the instance (this repo) with manual dispatch using the included GitHub action, or use auto-deploy when `config.yaml` is updated.


## Run locally for development

For running a local server, connecting to a local database:
```
source servers/localhost/dev_local.env
uvicorn seqcolapi.main:app --reload --port 8100
```

For running a local server, connecting to the production database:
```
source servers/seqcolapi.databio.org/production.env
export SEQCOLAPI_CONFIG=servers/seqcolapi.databio.org/seqcolapi.yaml
uvicorn seqcolapi.main:app --reload --port 8100
```

### Installing and running for production

Install natively with `pip install .`, then run natively:

```
source servers/seqcolapi.databio.org/production.env
seqcolapi serve -c /home/nsheff/code/seqcolapi/servers/seqcolapi.databio.org/seqcolapi.yaml -p 8100
```

Use at: http://localhost:8100

http://0.0.0.0:8100/comparison/a6748aa0f6a1e165f871dbed5e54ba62/2786eb8a921aa97018c214f64b9960a0

