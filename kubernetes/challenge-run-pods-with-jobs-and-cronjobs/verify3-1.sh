#!/bin/zsh

minikube kubectl -- get cronjob | grep hello-cronjob

minikube kubectl -- describe cronjob hello-cronjob | grep -A 20 Schedule | grep -A 20 busybox | grep echo
