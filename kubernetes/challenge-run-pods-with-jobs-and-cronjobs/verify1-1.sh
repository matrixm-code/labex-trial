#!/bin/zsh

minikube kubectl -- get jobs | grep hello-job

minikube kubectl -- describe job hello-job | grep -A 10 busybox | grep "echo"
