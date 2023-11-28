#! /usr/bin/bash

# Check if Hadoop is already installed
read -p "Have you already installed Hadoop? (yes/no): " answer

if [ "$answer" == "no" ]; then
    bash hadoop_installation.sh
fi


cd ~
wget https://archive.apache.org/dist/hbase/2.1.4/hbase-2.1.4-bin.tar.gz


tar xzf hbase-2.1.4-bin.tar.gz -C ~/hadoop

cd ~/hadoop/hbase-2.4.1-bin/bin


start-hbase.sh