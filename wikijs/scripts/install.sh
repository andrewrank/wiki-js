#!/bin/bash
sudo yum update -y
sudo yum install ec2-instance-connect
wget https://github.com/Requarks/wiki/releases/latest/download/wiki-js.tar.gz
mkdir wiki
tar xzf wiki-js.tar.gz -C ./wiki
cd ./wiki
mv config.sample.yml config.yml
