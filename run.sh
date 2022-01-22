#!/bin/bash 
./kill.sh 
nohup ./v2ray -c ./config.json > ./v2.log 2>&1 &
