#!/usr/bin/env bash

# 2.7G

# Bash config
cat >/home/ubuntu/.bash_profile <<EOF
export EC2_HOME=~/ec2-api-tools-1.6.8.1/bin
export PATH=$PATH:$EC2_HOME
export PATH=$PATH:.

alias ls='ls -laghFG'
alias ll='ls -laghFG'
alias l='ls -laghFG'

# Grep
alias grep='grep -n'
export GREP_OPTIONS='--color=auto'
export GREP_COLOR='1;35;40'

# Git
export PS1="\[\033[38m\]\u\[\033[32m\] \w \[\033[31m\]\`ruby -e \"print (%x{git branch 2> /dev/null}.split(%r{\n}).grep(/^\*/).first || '').gsub(/^\* (.+)$/, '(\1) ')\"\`\[\033[37m\]$\[\033[00m\] "
git config --global color.ui true
git config --global format.pretty oneline
git config --global core.autocrl input
git config --global core.fileMode true
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Ruby Version Manager
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*
EOF
chgrp -R ubuntu .bash_profile
chown -R ubuntu .bash_profile
cp /home/ubuntu/.bash_profile /root

source ~/.bashrc
source ~/.bash_profile

export DEBIAN_FRONTEND=noninteractive

sudo su

apt-get -y update


#############
# Nginx
sudo apt-get install libpcre3 libpcre3-dev

NGINX_VERSION = '1.7.4'
HEADERS_MODULE = '0.25'
rm -rf nginx-%s % NGINX_VERSION
wget http://nginx.org/download/nginx-%s.tar.gz % NGINX_VERSION
tar -xvzf nginx-%s.tar.gz % NGINX_VERSION
wget https://github.com/openresty/headers-more-nginx-module/archive/v%s.tar.gz % HEADERS_MODULE
tar -xvzf v%s.tar.gz % HEADERS_MODULE

# nginx_modules = ' '.join([
#     '--with-http_ssl_module',
#     '--add-module=../headers-more-nginx-module-%s' % HEADERS_MODULE,
#     '--with-http_stub_status_module'
#     '--with-http_gzip_static_module',
#     '--with-http_gunzip_module',
#     '--with-http_realip_module',
#     '--with-http_secure_link_module',
# ])

mkdir -p opt
with lcd('nginx-%s' % NGINX_VERSION):
    local('./configure --prefix=../opt/nginx %s' % nginx_modules)
    local('make')
    local('make install')
ln -sf `pwd`/opt/nginx/sbin/nginx .

./nginx -v
./nginx -t -p . -c etc/nginx.conf


#############
# EC2 SDK
wget http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip
unzip ec2-api-tools.zip
chgrp -R ubuntu ec2-api-tools-*
chown -R ubuntu ec2-api-tools-*
EC2_HOME=~/ec2-api-tools-1.6.8.1/bin
PATH=$PATH:$EC2_HOME

#############
# Base

apt-get -y install build-essential
apt-get -y install curl
apt-get -y install git-all
apt-get -y install autotools-dev
apt-get -y install cmake
apt-get -y install sqlite
apt-get -y install nmap

apt-get -y install python-pip
apt-get -y install python-dev
apt-get -y install python3.3
apt-get -y install python3.3-dev
apt-get -y install python3-pip # 3.2

pip install virtualenv
pip install nose
pip install coverage
pip install pyYAML
pip install simplejson
pip install jsonpickle
# pip-3.3 install virtualenv
# pip-3.3 install nose
# pip-3.3 install coverage
# pip-3.3 install pyYAML
# pip-3.3 install simplejson
# pip-3.3 install jsonpickle

pip install redis
pip install rq
pip install rq-scheduler
# pip-3.3 install redis
# pip-3.3 install rq
# pip-3.3 install rq-scheduler

# libtool, autoconf, automake
# uuid-dev

#############
# Languages

# Python
# python 2.7 and 3.2 installed
apt-get -y install pypy

# Ruby
# Ruby 1.9.3 installed
apt-get -y install ruby-dev
apt-get -y install rake
apt-get -y install rubygems
apt-get -y install ruby-rvm
# curl -L https://get.rvm.io | bash -s stable
gem install bundler

# Perl installed

# Java
apt-get -y install openjdk-6-jdk
apt-get -y install openjdk-7-jdk

# Scala
apt-get -y install scala

# Smalltalk
apt-get -y install gnu-smalltalk

# Groovy
apt-get -y install groovy

# Clojure
apt-get -y install clojure

# Lua
apt-get -y install lua50
apt-get -y install lua5.2
apt-get -y install luajit

# Objective C
apt-get -y install gobjc gnustep gnustep-make gnustep-common

# Javascript
apt-get -y install phantomjs
apt-get -y install libv8-3.8.9.20

# Go
apt-get -y install golang-go

# Erlang
apt-get -y install erlang

# Haskell
sudo apt-get -y install haskell-platform

# PHP
apt-get -y install php5

# C#
apt-get -y install mono-csharp-shell

#############
# Reports
gcc --version
g++ --version
python2.7 --version
python3.2 --version
python3.3 --version
python --version
pypy --version
ruby --version
java -version
scala -version
gst --version
groovy --version
clojure --eval "(clojure-version)"
perl --version
lua -v
go version
phantomjs --version
erl -noshell -eval 'io:fwrite("~s\n", [erlang:system_info(otp_release)]).' -s erlang halt
haskell-compiler --version
php --version
csharp --version

###################
# SSH config
cat >~/.ssh/config <<EOF
StrictHostKeyChecking no
EOF
# this stop the script
#exec ssh-agent bash
ssh-add
ssh-keygen -t rsa -C "user@domain" -N '' -f ~/.ssh/id_rsa
cp ~/.ssh/* /home/ubuntu/.ssh/
# pbcopy < ~/.ssh/id_rsa.pub


###################
# Clean up:
apt-get -y clean
df -h
