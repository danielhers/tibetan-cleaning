import os
import re

# key is syll string value is syll id
syllables = {}
with open(r'D:\Dev\tibetan-cleaning\syllables.txt', 'rb') as syll_file:
    for line in syll_file:
        arr = line.split(',')
        syllables[arr[0]] = int(arr[1])

# Key is stem id value is stem string
stems = {}
with open(r'D:\Dev\tibetan-cleaning\stems.txt', 'rb') as stem_file:
    for line in stem_file:
        arr = line.split(',')
        stems[int(arr[1])] = arr[0]

# key is syll id value is stem id
syll_stem = {}
with open(r'D:\Dev\tibetan-cleaning\SylToStem.txt', 'rb') as SylToStem_file:
    for line in SylToStem_file:
        arr = line.split(',')
        syll_stem[int(arr[0])] = int(arr[1])

syll_idf = dict(zip(syllables.keys(), [0] * len(syllables)))
stem_idf = dict(zip(stems.values(), [0] * len(stems)))
doc_size = 1000
file_num = 0
split_regex = re.compile("[^\w']+")

for root, subdirs, files in os.walk(r'D:\Dev\tibetan-cleaning\tokenize'):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as input_file:
                file_num += 1
                print 'Working on file count: ' + str(file_num) + ' file name:' + os.path.join(root, file)
                s = split_regex.split(input_file.read())
                i = 0
                while i < len(s):
                    temp_syls = []
                    temp_stms = []
                    while True:
                        temp_syl = s[i].lower()
                        if '|' in temp_syl:
                            temp_syl.replace('|', '')
                        if len(temp_syl) > 0 and temp_syl not in temp_syls:
                            temp_syls.append(temp_syl)

                            if temp_syl in syllables:
                                syll_idf[temp_syl] += 1
                                syll_id = syllables[temp_syl]
                                if syll_id in syll_stem:
                                    stem_id = syll_stem[syll_id]
                                    stem = stems[stem_id]
                                    if stem not in temp_stms:
                                        temp_stms.append(stem)
                                        stem_idf[stem] += 1
                        i += 1
                        if (i + 1) % doc_size == 0 or i >= len(s):
                            break
with open('syll_idf_docsize_' + str(doc_size) + '.csv', 'w') as syll_file:
    syll_file.write('syllable,idf\n')
    for key, value in sorted(syll_idf.items(), reverse=True, key=lambda x: x[1]):
        syll_file.write(key + ',' + str(value) + '\n')
with open('stem_idf_docsize_' + str(doc_size) + '.csv', 'w') as stem_idf_file:
    stem_idf_file.write('stem,idf\n')
    for key, value in sorted(stem_idf.items(), reverse=True, key=lambda x: x[1]):
        stem_idf_file.write(key + ',' + str(value) + '\n')
