#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_tide'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Tide</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'depth_id'},
				  $text{'depth_trend'},
				  $text{'depth_depth'},
				  $text{'depth_datum'},
				  $text{'depth_rise'},
				  $text{'depth_tide'},
				  $text{'depth_time'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from DEPTH_RISE_DATA order by WE_DATE_TIME desc limit 0,100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$id = $ref->{'DEPTH_ID'};
	$trend = $ref->{'TREND'};
	$depth = $ref->{'DEPTH'};
	$datum = $ref->{'DATUM'};
	$rise = $ref->{'RISE'};
	$tide = $ref->{'TIDE'};
	$time = $ref->{'WE_DATE_TIME'};
	print &ui_columns_row([
			$id,
			$trend,
			$depth,
			$datum,
			$rise,
			$tide,
			$time
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();


ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});