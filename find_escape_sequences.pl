#!/usr/bin/env perl

use strict;
use warnings;

sub uniq {
  my %seen;
  grep !$seen{$_}++, @_;
}

my @seqs;

while (<>) {
  push @seqs, /(&\w+;)/g;
}

@seqs = uniq(@seqs);
print "@seqs\n";
