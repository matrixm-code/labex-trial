#!/bin/zsh

POD_NAME=$(minikube kubectl -- get pods -l app=myapp -o jsonpath='{.items[*].metadata.name}')

minikube kubectl -- describe pod ${POD_NAME} | grep busybox
