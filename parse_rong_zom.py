# -*- coding: utf-8 -*-
import os
import re

INPUT_DIR = os.getcwd() + r'/' + 'Rong-zom_rawTexts'
OUTPUT_DIR = os.getcwd() + r'/' + 'Rong-zom_rawTexts_clean'

regex_tri = re.compile('<[^>]*>')
regex_sqr = re.compile('\[[^\]]*\]')
regex_space = re.compile(r"\s{2,}")
regex_space_begin = re.compile(r"^\s+")

for i in os.listdir(INPUT_DIR):
    if i.endswith(".txt"):
        print("reading " + i)
        with open(os.path.join(INPUT_DIR, i), 'r') as input_file:
            with open(os.path.join(OUTPUT_DIR, i), 'w') as output_file:
                s = input_file.read()
                s = s.replace('{', '(')
                s = s.replace('}', ')')
                s = s.replace("’", '\'')
                s = s.replace("?", '')
                s = s.replace(' | ', ' ')
                s = s.replace(' ||', '||')
                s = regex_tri.sub(' ', s)
                s = regex_sqr.sub(' ', s)
                s = regex_space.sub(' ', s)
                s = regex_space_begin.sub('', s)
                s = "".join(c.lower() if c.isupper() else c.upper() for c in s)
                output_file.write(s)
