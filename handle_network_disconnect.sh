#!/bin/bash

for (( i = 0; i < 50; i = i + 1)); do
    python3 dhu_connect.py USERNAME PASSWORD 5 2
    echo "hello world" $i
    sleep 10
done
exit 0
