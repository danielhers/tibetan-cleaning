#!/usr/bin/perl -n

use strict;
use warnings;

our %matches;
for my $token (split) {
    $matches{$token} = 1 if $token =~ /.*[aeiuoAEIUO].*[aeiuoAEIUO].*/;
}

END {
    $,="\n";
    print keys %matches;
}
