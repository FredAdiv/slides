use strict;
use warnings;
use feature 'say';

use MyMath qw(add);

if (scalar @ARGV != 2) {
    die "Usage: $0 X Y\n";
}

say add(@ARGV);


