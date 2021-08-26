#!/bin/bash

pip3 install --trusted-host pypi.org -r /root/tools/requirements.txt
python3 /root/apps/container_ti_sensortag_example.py 2>&1 >/dev/null