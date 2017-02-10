#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_solar'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Solar</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'solar_rad'},
				  $text{'solar_rad_hi'},
				  $text{'solar_energy'},
				  $text{'solar_lum'},
				  $text{'solar_uv'},
				  $text{'solar_time'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from SOLAR order by W_TIME desc limit 0, 100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$rad = $ref->{'RAD'};
	$rad_hi = $ref->{'RAD_HI'};
	$energy = $ref->{'ENERGY'};
	$lum = $ref->{'LUM'};
	$uv = $ref->{'UV'};
	$time = $ref->{'W_TIME'};
	print &ui_columns_row([
			$rad,
			$rad_hi,
			$energy,
			$lum,
			$uv,
			$time
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});