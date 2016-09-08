#!/bin/bash

NAME="lwaftr2"
CFG="lwaftr2.txt"
VMX="vmx-bundle-16.1R1.7.tgz"
CONTAINER="vmxlwaftr:v0.10"
IDENTITY="snabbvmx.key"
chmod 400 $IDENTITY
INTERFACES="0000:05:00.0/6"
LICENSE="license-eval.txt"

docker rm $NAME 2>/dev/null
docker run --name $NAME -ti --privileged -v $PWD:/u:ro $CONTAINER -I $IDENTITY -l $LICENSE -c $CFG $VMX $INTERFACES
docker rm $NAME
