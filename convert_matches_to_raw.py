#!/usr/bin/env python3
import argparse
import csv

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
    raw_matches = []
    raw_pos = [0, 0]
    clean_pos = [0, 0]
    for line in clean_matches:
        clean_start = [None, None]
        clean_end = [None, None]
        clean_start[0], clean_end[0], clean_start[1], clean_end[1] = map(int, line[:-1])
        score = line[-1]
        raw_start = [None, None]
        raw_end = [None, None]
        for i in (0, 1):
            raw_pos[i] += sum(len(s) + 1 for s in syllables[i][clean_pos[i]:clean_start[i]])
            clean_pos[i] = clean_start[i]
            raw_start[i] = raw_pos[i]
            raw_end[i] = raw_start[i] + sum(len(s) + 1 for s in syllables[i][clean_start[i]:clean_end[i]]) - 1
        raw_matches.append([raw_start[0], raw_end[0], raw_start[1], raw_end[1], score])

    if out_matches == "-":
        for line in raw_matches:
            print(",".join(map(str, line)))
    else:
        with open(out_matches, "w") as f:
            writer = csv.writer(f)
            writer.writerows(raw_matches)


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
