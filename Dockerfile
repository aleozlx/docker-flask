FROM ubuntu:16.04
RUN apt-get -y update && apt-get install -y build-essential vim git wget htop python3-dev python3-pip nginx
RUN pip3 install --upgrade pip && pip3 --no-cache-dir install Flask Celery
RUN mkdir -p /workspace "`python3 -m site --user-site`"
WORKDIR /workspace
CMD /bin/bash
