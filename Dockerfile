# Multi stage dockerfile to easily add custom packages

FROM python:3.7-slim AS compile-image
WORKDIR /packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt 
RUN pip3 install --prefix=/packages -r requirements.txt 

FROM gcr.io/spark-operator/spark-py:v3.1.1
COPY --from=compile-image /packages/lib/python3.7/site-packages /usr/lib/python3/dist-packages