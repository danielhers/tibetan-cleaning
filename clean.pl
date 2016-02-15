#!/usr/bin/perl -pi

use strict;
use warnings;

s%(\|\s*)?\@\d{1,3}[AB](\s*\*\|\|)?%%g;
s%(?<!\|)\|(?!\|)%%g;
s%[`#;]%%g;
s%&lt;%%g;
s%&amp;%%g;
s%\[\([^)]*\)\]%%g;
s%\s{2,}% %g;
s%^\s+%%g;
s%^\|\|\s*%%g;
s%\s+$%%g;
