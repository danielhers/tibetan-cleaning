#!/usr/bin/perl -npi

# Convert to TSV with columns:
# 1. Numeric identifier with leading digit representing book number
# 2. Line
# 3. null
# 4. Chapter identifier: 

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
