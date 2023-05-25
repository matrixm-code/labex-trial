#!/bin/zsh

minikube kubectl -- describe daemonset myapp-daemonset | grep -A 10 busybox | grep sleep
