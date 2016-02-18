#!/usr/bin/env python3
import argparse
import csv
from operator import itemgetter

"""
Example:
in_matches:
0,2,1,3,1.0
1,5,1,5,0.9

raw[1]:
bsgrubs grub drup gup shup

raw[2]:
par gpar spar dpar bar

out_matches:
0,12,4,13,1.0
8,26,4,22,0.9
"""


def convert_matches(in_matches, raw_files, out_matches):
    with open(in_matches) as f:
        reader = csv.reader(f)
        clean_matches = sorted(list(map(tuple, reader)))

    raw_text = []
    for file in raw_files:
        with open(file) as f:
            raw_text.append(f.read())

    syllables = tuple(map(str.split, raw_text))
    raw_matches = [[], []]

    # 0: txt 1 start, 1: txt 2 start, 2: txt 1 3ne, 3: txt 2 end
    clean_spans = [[], [], [], []]
    clean_spans[0], clean_spans[1], clean_spans[2], clean_spans[3], scores = zip(*clean_matches)
    for i in range(0, 4):
        clean_spans[i] = [int(x) for x in clean_spans[i]]

    (indices_txt2, clean_spans[1]) = zip(*sorted(enumerate(clean_spans[1]), key=itemgetter(1)))
    clean_spans[3] = [clean_spans[3][i] for i in indices_txt2]
    for i in (0, 1):
        raw_start = 0
        clean_pos = 0
        for match_num in range(0, len(clean_spans[0])):
            raw_start += sum(len(s) + 1 for s in syllables[i][clean_pos:clean_spans[i][match_num]])
            clean_pos = clean_spans[i][match_num]
            raw_end = raw_start + sum(
                len(s) + 1 for s in syllables[i][clean_pos:clean_spans[2 + i][match_num]]) - 1
            raw_matches[i].append((raw_start, raw_end))

    temp_raw_matches = [None] * len(raw_matches[1])
    for i in range(0, len(raw_matches[1])):
        temp_raw_matches[indices_txt2[i]] = raw_matches[1][i]
    raw_matches[1] = temp_raw_matches

    if out_matches == "-":
        for match_num in range(0, len(clean_spans[0])):
            print(str(raw_matches[0][match_num][0]) + ',' + str(
                raw_matches[1][match_num][0]) + ',' + str(raw_matches[0][match_num][1]) + ',' + str(
                raw_matches[1][match_num][1]) + ',' + scores[match_num] + + '\n')
    else:
        with open(out_matches, "w") as f:
            # writer = csv.writer(f)
            for match_num in range(0, len(clean_spans[0])):
                f.write(str(raw_matches[0][match_num][0]) + ',' + str(
                    raw_matches[1][match_num][0]) + ',' + str(raw_matches[0][match_num][1]) + ',' + str(
                    raw_matches[1][match_num][1]) + ',' + scores[match_num] + '\n')


def main():
    argparser = argparse.ArgumentParser(description="Convert a matches file with clean syllable spans "
                                                    "into a matches file with raw character spans.")
    argparser.add_argument("in_matches", help="CSV file with clean syllable spans")
    argparser.add_argument("raw", nargs=2, help="Raw text file")
    argparser.add_argument("-o", "--out_matches", default="-",
                           help="output CSV file with raw character spans")
    args = argparser.parse_args()
    convert_matches(args.in_matches, args.raw, args.out_matches)


if __name__ == "__main__":
    main()
