#!/usr/bin/perl -pi

use strict;
use warnings;

our %lexicon;
BEGIN {
    use Text::CSV::Simple;
    my $parser = Text::CSV::Simple->new;
    %lexicon = reverse map {@$_} $parser->read_file("stems.txt");
    $lexicon{0} = 0;
}

my @stems;
for my $stem_id (split) {
    push @stems, $lexicon{$stem_id} // -1;
}
$_ = join(" ", @stems);