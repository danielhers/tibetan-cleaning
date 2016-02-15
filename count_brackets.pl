#!/usr/bin/env perl

use strict;
use warnings;

my $brackets = 0;

while (<>) {
  $brackets += () = /\[(?!\()/g;
}

print "$brackets\n";
