#!/usr/bin/perl -pi

use strict;
use warnings;

our %lexicon;
BEGIN {
    use Text::CSV::Simple;
    my $parser = Text::CSV::Simple->new;
    %lexicon = map {@$_} $parser->read_file("syllables.txt");
    $lexicon{0} = 0;
}

my @ids;
for my $token (split) {
    push @ids, $lexicon{lc $token} // -1;
}
$_ = join(" ", @ids);