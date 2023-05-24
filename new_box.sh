#!/usr/bin/bash

cd ~/OSCP && mkdir $1
cd $1 && mkdir Writeup && cd Writeup
cp ~/OSCP/OSCP-Writeup.tex . && mv OSCP-Writeup.tex $1-en.tex
mkdir resources 
