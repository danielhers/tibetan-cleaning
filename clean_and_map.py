import argparse
import os


replacers = []


def merge(mapping, r):
    for i, ((clean_start, clean_end), raw) in enumerate(mapping):
        if clean_end <= r.raw_start:
            pass

def clean_and_map(infile, outfile, mapfile):
    with open(infile) as f:
        s = f.read()
    mapping = []
    for replacer in replacers:
        r = replacer(s)
        s = r.apply(s)
        merge(mapping, r)
    with open(outfile, "w") as f:
        f.write(s)
    with open(mapfile, "w") as f:
        f.writelines(",".join(i for span in spans for i in span) + "\n" for spans in mapping)


def main():
    argparser = argparse.ArgumentParser(description='Clean files and map spans.')
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
