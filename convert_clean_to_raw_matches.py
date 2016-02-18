#!/usr/bin/env python3
import argparse
import csv


def convert_matches(in_matches, mapping, out_matches):
    with open(in_matches) as f:
        clean_matches = sorted(list(map(tuple, csv.reader(f))))

    with open(mapping[0]) as f:
        mapping1 = [(int(c), int(r)) for c, r in csv.reader(f)]

    with open(mapping[1]) as f:
        mapping2 = [(int(c), int(r)) for c, r in csv.reader(f)]

    raw_matches = []
    for clean_start1, clean_start2, clean_end1, clean_end2, score in clean_matches:
        clean_start1, clean_start2, clean_end1, clean_end2 = map(
            int, (clean_start1, clean_start2, clean_end1, clean_end2))
        raw_start1 = next(r for c, r in reversed(mapping1) if c <= clean_start1)
        raw_start2 = next(r for c, r in reversed(mapping2) if c <= clean_start2)
        raw_end1 = next(r for c, r in mapping1 if c >= clean_end1)
        raw_end2 = next(r for c, r in mapping2 if c >= clean_end2)
        raw_matches.append(map(str, (raw_start1, raw_start2, raw_end1, raw_end2, score)))

    with open(out_matches, "w") as f:
        f.writelines(",".join(m) + "\n" for m in raw_matches)


def main():
    argparser = argparse.ArgumentParser(description="Convert a matches file with clean syllable spans "
                                                    "into a matches file with raw character spans.")
    argparser.add_argument("in_matches", help="CSV file with clean syllable spans")
    argparser.add_argument("mapping", nargs=2, help="CSV file with clean to raw mapping")
    argparser.add_argument("-o", "--out_matches", default="-",
                           help="output CSV file with raw character spans")
    args = argparser.parse_args()
    convert_matches(args.in_matches, args.mapping, args.out_matches)


if __name__ == "__main__":
    main()
