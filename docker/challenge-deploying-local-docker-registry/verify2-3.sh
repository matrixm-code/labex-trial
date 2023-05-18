#!/bin/zsh

cat ~/.zsh_history | grep docker | grep push

test -d "/home/labex/dockerregistry/docker/registry/v2/repositories/hello-world"
