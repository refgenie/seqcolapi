FROM databio/seqcolapi

COPY config/seqcolapi.yaml /seqcolapi_config.yaml

ENTRYPOINT ["seqcolapi", "serve", "-c", "/seqcolapi_config.yaml"]
