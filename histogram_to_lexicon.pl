#!/usr/bin/perl -p

use strict;
use warnings;

s%\(\d+,\s*(.*)\)%$1,$.%;