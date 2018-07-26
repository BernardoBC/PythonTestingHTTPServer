#!/bin/sh
git fetch origin
git reset --hard origin/master
python3 ./helloworld.py