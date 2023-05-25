#!/bin/zsh

minikube kubectl -- get pods | grep myapp-pod

minikube kubectl -- describe pod myapp-pod | grep -A 5 nginx | grep Port | grep 80
