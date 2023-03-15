#!/bin/bash
ARCH=$(uname -m)

VERSION=0.1.0
BASEIMAGE=3.9.15-bullseye
SUFFIX=${VERSION}-bullseye-${ARCH}

# Build the base image
docker build -t interactive_analysis/maintenance:${SUFFIX} \
    --build-arg ARCH=${ARCH} \
    --build-arg BASEIMAGE=${BASEIMAGE} \
    -f scripts/Dockerfile.maint . 

docker tag registry.example.com/interactive_analysis/maintenance:${SUFFIX} interactive_analysis/maintenance:${SUFFIX}
