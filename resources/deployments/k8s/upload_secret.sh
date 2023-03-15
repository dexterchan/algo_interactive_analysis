#!/bin/bash

# This script creates a secret in the kubernetes cluster
kubectl delete secret aws-secret -n backtest-crypto
kubectl create secret generic aws-secret -n backtest-crypto --from-file=aws_credential.json=resources/.secret/aws_credential.json