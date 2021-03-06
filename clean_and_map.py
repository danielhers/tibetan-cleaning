import argparse
import os
import re


substitutions = (
    (r"\?+|"
     r"^(?:\|\s*)?@\d{1,3}[AB]\s*[*#]*\s*\|\|\s*|"
     r"\s*(?:\|\s*)?@\d{1,3}[AB]\s*[*#]*\s*|"
     r"&lt;(?:(?!&gt;).)*&gt;|"
     r"(?<!\|)\|(?!\|)|"
     r"<[^>]*>|"
     r"^\s+|"
     r"\s$|"
     r"(?<=\s)\[[^\]]*\]\s*|"
     r"^\s*\|\|\s*", ""),
    (r"\s*\[\([^)]*\)\]\s*|"
     r"\s{2,}|"
     r"\s*(?<!\|)\|(?!\|)\s*|"
     r"\s*&lt;\s*|"
     r"\s*&amp;\s*|"
     r"\s*[`#;\s]+\s*|"
     r"\s*\[[^\]]*\]\s+|"
     r"\s*\d+\s*|"
     r"\s*\.{2,}\s*", " "),
    (r"(?<!\s)[*#]*\|\|\s*", " ||\n"),
    (r"(?<=\s)[*#]*\|\|\s*", "||\n"),
)

pattern = re.compile("|".join("(" + s[0] + ")" for s in substitutions))


def clean_and_map(infile, outfile, mapfile):
    with open(infile) as f:
        raw = f.read()
    raw = raw.replace("{", "(").replace("}", ")").replace("’", "\"")
    mapping = [(0, 0)]
    clean = ""
    last_raw_end = 0
    for m in pattern.finditer(raw):
        clean += raw[last_raw_end:m.start()]
        mapping.append((len(clean), m.start()))
        clean += substitutions[m.lastindex - 1][1]
        last_raw_end = m.end()
        mapping.append((len(clean), last_raw_end))
    clean += raw[last_raw_end:]
    mapping.append((len(clean), len(raw)))
    with open(outfile, "w") as f:
        f.write(clean)
    with open(mapfile, "w") as f:
        f.writelines(",".join(map(str, offsets)) + "\n" for offsets in mapping)


def main():
    argparser = argparse.ArgumentParser(description="Clean files and map spans.")
    argparser.add_argument("indir", help="Input directory")
    argparser.add_argument("outdir", help="Output directory")
    args = argparser.parse_args()

    for root, _, files in os.walk(args.indir):
        for name in files:
            infile = os.path.join(root, name)
            outfile = os.path.join(args.outdir, name)
            mapfile = os.path.splitext(outfile)[0] + ".map"
            clean_and_map(infile, outfile, mapfile)

if __name__ == "__main__":
    main()
