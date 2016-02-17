import argparse
import os
import re


substitutions = (
    (r"\?+|"
     r"&lt;(?:(?!&gt;).)*&gt;|"
     r"<[^>]*>|"
     r"^\s+|"
     r"\s$"
     r"^\|\|\s*", ""),
    (r" \|\|", "\|\|"),
    (r"\[\([^)]*\)\]|"
     r"\s{2,}|"
     r"(?:\|\s*)?@\d{1,3}[AB](?:\s*\*\|\|)?|"
     r"(?<!\|)\|(?!\|)|"
     r"&lt;|"
     r"&amp;|"
     r"[`#;]|"
     r"\[[^\]]*\]|"
     r"\d+|"
     r"\.{2,}|"
     r"\s{2,}", " "),
)

pattern = re.compile("|".join("(" + s[0] + ")" for s in substitutions))


def clean_and_map(infile, outfile, mapfile):
    with open(infile) as f:
        raw = f.read()
    raw = raw.replace("{", "(")
    raw = raw.replace("}", ")")
    raw = raw.replace("’", "\"")
    mapping = [(0, 0)]
    clean = ""
    last_raw_end = 0
    for m in pattern.finditer(raw):
        clean += raw[last_raw_end:m.start()]
        mapping.append((len(clean), m.start()))
        clean += substitutions[m.lastindex - 1]
        last_raw_end = m.end()
        mapping.append((len(clean), last_raw_end))
    clean += raw[last_raw_end:]
    with open(outfile, "w") as f:
        f.write(s)
    with open(mapfile, "w") as f:
        f.writelines(",".join(i for span in spans for i in span) + "\n" for spans in mapping)


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
