#!/bin/bash
ARCH=$(uname -m)

VERSION=0.1.0
BASEIMAGE=3.9.15-bullseye
CONDA_VERSION=39_23.1.0-1
CONDA_VERSION=39_4.9.2
SPARK_VERSION=3.4.0
SUFFIX=${VERSION}-bullseye-${ARCH}

# Build the base image
docker build -t interactive_analysis/jupyter_notebook:${SUFFIX} \
    --build-arg ARCH=${ARCH} \
    --build-arg BASEIMAGE=${BASEIMAGE} \
    --build-arg CONDA_VERSION=${CONDA_VERSION} \
    --build-arg SPARK_VERSION=${SPARK_VERSION} \
    --target final \
    -f scripts/Dockerfile . 

docker tag interactive_analysis/jupyter_notebook:${SUFFIX} registry.example.com/interactive_analysis/jupyter_notebook:${SUFFIX}
