FROM tiangolo/uvicorn-gunicorn:python3.8-slim
LABEL authors="Nathan Sheffield"

COPY . /app
RUN pip install https://github.com/databio/henge/archive/new_array_handling.zip
RUN pip install https://github.com/refgenie/refget/archive/dev.zip
RUN pip install https://github.com/refgenie/seqcol/archive/dev.zip
RUN pip install .

