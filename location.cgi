#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_location'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Location</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'location_lat'},
				  $text{'location_long'},
				  $text{'location_cog'},
				  $text{'location_sog'},
				  $text{'location_time'}],
				100, 0, \@tds);


$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from LOCATION order by W_TIME desc limit 0, 100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$lat = $ref->{'LAT'};
	$long = $ref->{'LONG'};
	$cog = $ref->{'COG'};
	$sog = $ref->{'SOG'};
	$time = $ref->{'W_TIME'};
	print &ui_columns_row([
			$lat,
			$long,
			$cog,
			$sog,
			$time
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});