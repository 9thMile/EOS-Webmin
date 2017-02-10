#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_wind'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Wind</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'wind_speed'},
				  $text{'ap_wind_speed'},
				  $text{'wind_high'},
				  $text{'ap_wind_dir'},
				  $text{'wind_dir'},
				  $text{'wind_rose'},
				  $text{'wind_time'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from WIND order by W_TIME desc limit 0, 100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$speed = $ref->{'SPEED'};
	$apspeed = $ref->{'AP_SPEED'};
	$hi_speed = $ref->{'HI_GUST'};
	$apdir = $ref->{'AP_DIRECTION'};
	$dir = $ref->{'DIRECTION'};

	$rose = $ref->{'ROSE'};
	$time = $ref->{'W_TIME'};
	print &ui_columns_row([
			$speed,
			$apspeed,
			$hi_speed,
			$apdir,
			$dir,
			$rose,
			$time
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});