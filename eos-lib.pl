=head1 eos-lib.pl

Functions for managing the Foobar webserver configuration file.

  foreign_require("eos", "eos-lib.pl");
  @sites = eos::list_eos_websites()

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

=head2 get_eos_config()

Returns the EOS Webserver configuration as a list of hash references with name and value keys.

=cut
sub get_eos_config
{
my $lref = &read_file_lines($config{'eos_conf'});
my @rv;
my $lnum = 0;
foreach my $line (@$lref) {
    my ($n, $v) = split(/\s+/, $line, 2);
    if ($n) {
      push(@rv, { 'name' => $n, 'value' => $v, 'line' => $lnum });
      }
    $lnum++;
    }
return @rv;
}