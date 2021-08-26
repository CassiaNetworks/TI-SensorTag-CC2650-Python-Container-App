#!/bin/bash

python_version=$(python3 --version)
old_python_version="3.5"

# If the current Python version has 3.5 in it
# (default container v1.1.1 python3 version is 3.5.2), update it to 3.9.6.
# WARNING: This section could take a long time to run! It should only run once.
#          After upgrading from Python 3.5.2 to 3.9.6, this section is skipped.
if [[ "$python_version" == *"$old_python_version"* ]]; then 
    mkdir ~/python3_9_6
    cd ~/python3_9_6
    wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
    tar zxfv Python-3.9.6.tgz
    find ~/python3_9_6 -type d | xargs chmod 0755
    cd Python-3.9.6
    #./configure --prefix=$HOME/python3
    #make && make install
    cp python python3
    mkdir python3path
    mv python3.9 python3path/
    export PATH=$HOME/python3_9_6/Python-3.9.6/python3path:$PATH

    
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py --user
fi

pip3 install -r /root/tools/requirements.txt
#python3.9 /root/apps/container_ti_sensortag_example.py 2>&1 >/dev/null
python3 /root/apps/container_ti_sensortag_example.py 2>&1 >/dev/null