#!/usr/bin/perl -n

# Convert to TSV with columns:
# 1. Numeric identifier with leading digit representing book number
# 2. Line text
# 3. NULL
# 4. Chapter identifier: full file path starting from the corpus directory,
#                        followed by a single space and the chapter identifier
#                        (@\d{1,3}[AB])

use strict;
use warnings;

my $line_id;
my $chapter;
BEGIN {
    use bigint;
    $line_id = 10000001;
    $chapter = "";
}

s%(?<!\|)\|(?!\|)%%g;
s%[`#;]%%g;
s%&lt;%%g;
s%&amp;%%g;
s%\[\([^)]*\)\]%%g;
s%\s{2,}% %g;
s%^\s+%%g;
s%^\|\|\s*%%g;
s%\s+$%%g;

for my $line (split /\|\|\s*/) {
    $line =~ s/\s*(\|\s*)?(\@\d{1,3}[AB])(\s*\*\|\|)?\s*/$chapter = $2; ''/ge;
    print join("\t", ($line_id++, $line, "NULL", "$ARGV $chapter")), "\n";
}