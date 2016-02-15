#!/usr/bin/perl -pi

use strict;
use warnings;

s%\s*(\|\|)\s*% $1 %g;
s%\s*(?<!\|)(\|)(?!\|)\s*% $1 %g;
s%\[[^\]]\]\s*%%;
s%\s*$% %g;
