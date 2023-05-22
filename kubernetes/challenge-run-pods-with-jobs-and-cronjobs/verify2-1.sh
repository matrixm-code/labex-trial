#!/bin/zsh

minikube kubectl -- get jobs | grep download-job

minikube kubectl -- describe job download-job | grep -A 20 Containers | grep -A 20 "http://example.com/file" | grep -A 10 /data | grep EmptyDir
