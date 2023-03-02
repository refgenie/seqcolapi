
docker run --rm -p 8000:8000 --name sccon \
  --env "POSTGRES_PASSWORD" \
  --env "POSTGRES_DB" \
  --env "POSTGRES_HOST" \
  --env "POSTGRES_USER" \
  --volume $CODE/seqcolapi.databio.org/config/seqcolapi.yaml:/config.yaml \
  scim seqcolapi serve -c /config.yaml -p 8000