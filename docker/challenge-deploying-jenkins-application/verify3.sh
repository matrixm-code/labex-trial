#!/bin/zsh

docker ps | grep jenkins-docker | grep "8080.*50000\|50000.*8080"
