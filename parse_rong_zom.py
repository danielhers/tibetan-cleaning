# -*- coding: utf-8 -*-
import os
import re

INPUT_DIR = os.getcwd() + r'/' + 'Rong-zom_rawTexts2'
OUTPUT_DIR = os.getcwd() + r'/' + 'Rong-zom_rawTexts_clean2'

regex_tri = re.compile('&lt;((?!&gt;).)*&gt;|<[^>]*>')
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
                s = s.swapcase()
                output_file.write(s)
