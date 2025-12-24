FROM nvidia/cudagl:11.3.0-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's@http://archive.ubuntu.com@http://mirrors.aliyun.com@g' /etc/apt/sources.list && apt update -y && \
    apt-get install -y --no-install-recommends build-essential git \
    wget vim tmux libtool autoconf automake libssl-dev libx11-dev \
    zlib1g-dev libxcursor-dev libxi-dev libxrandr-dev ninja-build \
    lsb-release python3-pip libxinerama-dev iwyu && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.8

RUN pip3 install --no-cache-dir cmake -i https://mirrors.aliyun.com/pypi/simple && \
    apt-get clean
