#!/bin/zsh

minikube kubectl -- get daemonsets | grep myapp-daemonset

minikube kubectl -- describe daemonset myapp-daemonset | grep -A 10 nginx | grep Port | grep 80
