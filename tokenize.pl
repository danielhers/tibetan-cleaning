#!/usr/bin/perl -p

use strict;
use warnings;

s%\s*(\|\|)\s*% $1 %g;
s%\s*(?<!\|)(\|)(?!\|)\s*% $1 %g;
s%\[[^\]]\]\s*%%;
s%\s*$% %g;
