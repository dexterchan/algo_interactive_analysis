ARG BASEIMAGE
ARG CONDA_VERSION
ARG ARCH
ARG RUN_DIR="/var/task"
ARG RUN_USER="appuser"
ARG TA_LIB_VERSION="0.4.0"


FROM python:${BASEIMAGE} as base
ARG RUN_DIR
ARG RUN_USER
ARG CONDA_VERSION
ARG ARCH

WORKDIR /tmp
ENV APPUSER=${RUN_USER}
ENV MINICONDA_SCRIPT="Miniconda3-py${CONDA_VERSION}-Linux-${ARCH}.sh"
#https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-aarch64.sh
RUN apt-get update -y && \
    apt-get upgrade -y && \ 
    apt-get install -y python3-pip wget 
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk
RUN mkdir -p ${RUN_DIR}
RUN groupadd --system --gid=9999  ${APPUSER} && \
    useradd --system --home-dir $RUN_DIR --uid=9999 --gid=${APPUSER} ${APPUSER}

RUN wget -O ${MINICONDA_SCRIPT} "https://repo.anaconda.com/miniconda/${MINICONDA_SCRIPT}" 
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
ENV CONDA_DIR=/var/conda
RUN sh ${MINICONDA_SCRIPT} -b -p $CONDA_DIR/miniconda -f 
ENV PATH=$CONDA_DIR/miniconda/bin:$PATH
ENV LD_LIBRARY_PATH=$CONDA_DIR/miniconda/lib:$LD_LIBRARY_PATH
RUN eval "$(conda shell.bash hook)" && \
    chmod 755 $CONDA_DIR && \
    chown -R ${APPUSER}:${APPUSER} $CONDA_DIR && \
    chown -R ${APPUSER}:${APPUSER} $RUN_DIR && \
    conda init
RUN apt-get remove wget -y

FROM base as builder
ARG RUN_DIR
ARG RUN_USER
ARG CONDA_VERSION
ARG ARCH
ARG TA_LIB_VERSION

RUN apt-get update -y && \
    apt-get upgrade -y && \ 
    apt-get install -y python3-pip wget gcc make libssl-dev libffi-dev python3-dev && \
    apt-get --reinstall install -y  apt-transport-https libssl-dev libffi-dev
# required to patch the pyOpenSSL for latest version with pip
RUN python3 -m pip install pyOpenSSL --upgrade
# required to patch the TA-LIB for latest version with pip
RUN tar xzf ta-lib-${TA_LIB_VERSION}-src.tar.gz  \
    && cd ta-lib \
    && ./configure --prefix=/usr --build=$(uname -m)-unknown-linux-gnu\
    && make && make install \
    && cd /tmp \
    && rm -Rf /tmp/ta-lib \
    && rm -f ta-lib-${TA_LIB_VERSION}-src.tar.gz
#RUN python3 -m pip install TA-Lib>=${TA_LIB_VERSION}



FROM base as final
ARG RUN_DIR
ARG RUN_USER
ARG CONDA_DIR
ARG ARCH
ARG TA_LIB_VERSION

# 
# COPY --chown=$RUN_USER --from=builder ${RUNDIR} ${RUNDIR}
COPY --chown=$RUN_USER --from=builder /usr/lib/libta_lib* /usr/lib/
COPY --chown=$RUN_USER --from=builder /usr/include/ta-lib/ /usr/include/ta-lib/
#COPY --chown=$RUN_USER --from=builder ${CONDA_DIR} ${CONDA_DIR}
RUN conda config --add channels conda-forge
RUN conda install mamba -c conda-forge -y
COPY scripts/environment.txt /tmp/environment.txt
RUN mamba install -y -c conda-forge  --file /tmp/environment.txt
RUN python3 -m pip install TA-Lib>=${TA_LIB_VERSION}
RUN python3 -m pip install pyOpenSSL --upgrade


ENV DATA_DIR=${RUN_DIR}/data
RUN mkdir -p ${DATA_DIR}
RUN chown -R ${RUN_USER}:${RUN_USER} ${DATA_DIR}
RUN mkdir -p ${RUN_DIR}/workspace
RUN chown -R ${RUN_USER}:${RUN_USER} ${RUN_DIR}/workspace

EXPOSE 8888
USER $RUN_USER
WORKDIR ${RUN_DIR}/workspace
CMD ["jupyter", "lab","--ip","0.0.0.0","--allow-root"]