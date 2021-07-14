use lib "$ENV{HOME}/src/bioperl-1.6.924";
use lib "$ENV{HOME}/src/ensembl/modules";
use lib "$ENV{HOME}/src/ensembl-compara/modules";
use lib "$ENV{HOME}/src/ensembl-variation/modules";
use lib "$ENV{HOME}/src/ensembl-funcgen/modules";
use warnings;
use strict;
use feature 'say';

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';

$registry->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous',
);

my $species = 'human';
my $group = 'variation'; # database type

my $dba = $registry->get_DBAdaptor($species,$group);

my $available_adaptors = $dba->get_available_adaptors;

# Display the list of adaptors available in the Ensembl Variation API
foreach my $adaptor (sort(keys(%$available_adaptors))) {
  print $available_adaptors->{$adaptor}."\n";
}

print "Hello";
print $ARGV[0]