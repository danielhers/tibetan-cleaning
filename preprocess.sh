#!/usr/bin/env bash

DIR=$(dirname $0)
#prev=raw
#for step in clean tokenize enumerate enum_stem stem; do
prev=tokenize
for step in enumerate enum_stem stem; do
    echo Running "'$step'"
    rm -rfv "$step"/*
    rm "$step".zip
    mkdir -p "$step"
    cp -rv "$prev"/* "$step"/
    "$DIR"/"$step".pl "$step"/Kangyur_Lhasa/*/* "$step"/TENGYUR_ACIP/*/*/*
#    zip -r "$step" "$step"/
    prev="$step"
done
echo Done