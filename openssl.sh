#!/usr/bin/env bash

echo This is my super secret message! > mesg.txt

openssl aes-128-cbc -in mesg.txt -base64 -out ciph.txt -k thebirdistheword

hexdump ciph.txt > hex.txt

openssl aes-128-cbc -d -in ciph.txt -base64 -out plain.txt -k thebirdistheword

cat mesg.txt ciph.txt hex.txt plain.txt

