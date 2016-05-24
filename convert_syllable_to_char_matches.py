#!/usr/bin/env python3
import argparse
import csv
from operator import itemgetter

def get_syllable_to_char_map(txt):
    tokens = txt.split(' ')
    token_start = [None]*len(tokens)
    token_end =[None]*len(tokens)
    token_start[0] = 0
    token_end[0] = len(tokens[0])
    for i in range(1,len(tokens)):
        token_start[i] = token_end[i-1] + 1
        token_end[i] = token_start[i] + len(tokens[i])

    return (token_start , token_end)

def convert_matches(in_matches, raw_files, out_matches):

    raw_text = []
    for file in raw_files:
        with open(file) as f:
            raw_text.append(f.read())

    file_mapping = []
    for txt in raw_text:
        file_mapping.append(get_syllable_to_char_map(txt))

    with open(in_matches) as fin:
        reader = csv.reader(fin)
        with open(out_matches, "wb") as fout:
            writer = csv.writer(fout)
            for line in reader:
                writer.writerow([
                    str(file_mapping[0][0][int(line[0])]),
                    str(file_mapping[1][0][int(line[1])]),
                    str(file_mapping[0][1][int(line[2])]),
                    str(file_mapping[1][1][int(line[3])]),
                    line[4]
                ])


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