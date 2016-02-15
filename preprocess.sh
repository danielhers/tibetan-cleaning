#!/usr/bin/env bash -x

DIR=$(dirname $0)
rm -rf clean/*
cp -r Kangyur_Lhasa TENGYUR_ACIP clean/
"$DIR"/clean.pl clean/Kangyur_Lhasa/*/* clean/TENGYUR_ACIP/*/*/*
rm -rf tokenized/*
cp -r clean/* tokenized/
"$DIR"/tokenize.pl tokenized/Kangyur_Lhasa/*/* tokenized/TENGYUR_ACIP/*/*/*
rm -rf enumerated/*
cp -r tokenized/* enumerated/
"$DIR"/enumerate.pl enumerated/Kangyur_Lhasa/*/* enumerated/TENGYUR_ACIP/*/*/*
echo done