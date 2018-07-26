#!/bin/sh
git fetch origin
git reset --hard origin/master
chmod +x helloworld.py
python3 ./helloworld.py