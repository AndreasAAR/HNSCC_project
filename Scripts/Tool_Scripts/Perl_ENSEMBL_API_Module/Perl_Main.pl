use lib "$ENV{HOME}/src/bioperl-1.6.924";
use lib "$ENV{HOME}/src/ensembl/modules";
use lib "$ENV{HOME}/src/ensembl-compara/modules";
use lib "$ENV{HOME}/src/ensembl-variation/modules";
use lib "$ENV{HOME}/src/ensembl-funcgen/modules";

use warnings;
use strict;
use feature 'say';

print "Hello";
print $ARGV[0]