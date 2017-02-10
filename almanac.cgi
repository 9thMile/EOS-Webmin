#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_almanac'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS ALMANAC</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'Almanac_Day'},
				  $text{'Almanac_Sunrise'},
				  $text{'Almanac_Sunset'},
				  $text{'Almanac_Solarmax'},
				  $text{'Almanac_Solaralt'},
				  $text{'Almanac_Daylength'},
				  $text{'Almanac_Moonphase'},
				  $text{'Almanac_Moonfull'}],
				100, 0, \@tds);


$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from ALMANAC order by WE_DATE desc limit 0, 50";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$day = $ref->{'WE_DATE'};
	$rise = $ref->{'SUNRISE'};
	$set = $ref->{'SUNSET'};
	$smax = $ref->{'SOLARMAX'};
	$salt = $ref->{'SOLAR_ALT'};
	$dl = $ref->{'DAY_LENGTH'};
	$phase = $ref->{'MOONPHASE'};
	$full = $ref->{'MOONFULLNESS'};
	print &ui_columns_row([
			$day,
			$rise,
			$set,
			$smax,
			$salt,
			$dl,
			$phase,
			$full], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});