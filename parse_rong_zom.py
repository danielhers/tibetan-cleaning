# -*- coding: utf-8 -*-
import os, re

INPUT_DIR = os.getcwd() + r'/' + 'Rong-zom_rawTexts'
OUTPUT_DIR = os.getcwd() + r'/' + 'Rong-zom_rawTexts_clean'

regex_tri = re.compile(r'<[^>]*>')
regex_sqr = re.compile(r'\[[^\]]*\]')
regex_space = re.compile(r"\s{2,}")

for i in os.listdir(INPUT_DIR):
    if i.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, i), 'rb') as input_file:
            with open(os.path.join(OUTPUT_DIR, i), 'wb') as output_file:
                for line in input_file:
                    line = line.replace('{', '(')
                    line = line.replace('}', ')')
                    line = line.replace("’", '\'')
                    line = line.replace("?", '')


                    line = line.replace(' | ', ' ')
                    line = line.replace(' ||', '||')
                    line = regex_tri.sub(' ', line)
                    line = regex_sqr.sub(' ', line)
                    line = regex_space.sub(' ', line)
                    output_file.writelines(line)
        continue
    else:
        continue
