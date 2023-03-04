#!/bin/bash

docker run -it --rm -p 8888:8888 \
        -v $(pwd)/notebooks:/var/task/workspace\
         interactive_analysis/jupyter_notebook:0.1.0-bullseye-x86_64 