#!/usr/bin/perl -p

use strict;
use warnings;

my %lexicon;
BEGIN {
    my $parser = Text::CSV::Simple->new;
    $parser->field_map(qw/syllable id/);
    %lexicon = $parser->read_file("lexicon.txt");
}

my @ids;
for $token (split) {
    push @ids, $lexicon[$token] // -1;
}
print join(" ", @ids);