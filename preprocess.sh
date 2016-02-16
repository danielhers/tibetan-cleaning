#!/usr/bin/env bash

DIR=$(dirname $0)
prev=raw
for step in clean tokenize enumerate; do
    echo Running "'$step'"
    rm -rfv "$step"/*
    mkdir -p "$step"
    cp -rv "$prev"/* "$step"/
    "$DIR"/"$step".pl "$step"/Kangyur_Lhasa/*/* "$step"/TENGYUR_ACIP/*/*/*
    zip -r "$step" "$step"/
    prev="$step"
done
echo Done