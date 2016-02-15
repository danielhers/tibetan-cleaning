#!/usr/bin/env perl

use strict;
use warnings;

my $special = 0;

while (<>) {
  $special += () = /[^[:ascii:]]/g;
}

print "$special\n";
