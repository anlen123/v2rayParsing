#!/bin/bash 
ps -ef | grep v2ray | grep -v grep  | awk '{print $2}' | xargs kill -9
