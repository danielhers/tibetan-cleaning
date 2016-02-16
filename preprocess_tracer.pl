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

our $line_id;
our $chapter;
our %syllable_to_id;
our %syllable_id_to_stem_id;
our %stem_id_to_stem;
BEGIN {
    $line_id = 1;
    $chapter = "";

    use Text::CSV::Simple;
    my $parser = Text::CSV::Simple->new;
    %syllable_to_id = map {@$_} $parser->read_file("syllables.txt");
    %syllable_id_to_stem_id = map {@$_} $parser->read_file("SylToStem.txt");
    %stem_id_to_stem = reverse map {@$_} $parser->read_file("stems.txt");
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
    my @stems = ();
    for my $syllable (split /\s+/, $line) {
        my $syllable_id = $syllable_to_id{lc $syllable} // -1;
        my $stem_id = $syllable_id_to_stem_id{$syllable_id} // -1;
        my $stem = $stem_id_to_stem{$stem_id} // $syllable;
        push @stems, $stem;
    }
    $line = join(" ", @stems);
    print join("\t", ($line_id++, $line, "NULL", "$ARGV $chapter")), "\n";
}