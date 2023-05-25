#!/bin/zsh

docker ps | grep registry | grep 5000 | grep my-registry

docker inspect my-registry | grep dockerregistry
