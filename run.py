#!/usr/bin/python3
from __future__ import print_function
import os, sys

DOCKER="docker"
IMAGE="aleozlx/flask-app:latest"
PORTS = ['-p', '8084:5000']
VOLUMNS = ['-v', os.path.abspath('./app')+':/workspace']

argv = [DOCKER, 'run', '-it'] + PORTS + VOLUMNS + [IMAGE] + ['/workspace/run.sh']
os.execvp(DOCKER, argv)
