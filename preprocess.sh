#!/usr/bin/env bash

./clean.pl Kangyur_Lhasa/*/* TENGYUR_ACIP/*/*/*
./tokenize.pl Kangyur_Lhasa/*/* TENGYUR_ACIP/*/*/*
./enumerate.pl Kangyur_Lhasa/*/* TENGYUR_ACIP/*/*/* >mapped.txt