#!/usr/bin/perl -pi

use strict;
use warnings;

our %lexicon;
BEGIN {
    use Text::CSV::Simple;
    my $parser = Text::CSV::Simple->new;
    %lexicon = reverse map {@$_} $parser->read_file("syllable-lexicon.txt");
}

my @ids;
for my $token (split) {
    push @ids, $lexicon{$token} // -1;
}
$_ = join(" ", @ids);