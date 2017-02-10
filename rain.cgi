#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_rain'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Temp</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'rain_rate'},
				  $text{'rain_amount'},
				  $text{'rain_fall_today'},
				  $text{'rain_fall_yesterday'},
				  $text{'rain_tips'},
				  $text{'rain_time'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from RAIN order by W_TIME desc limit 0, 100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$rate = $ref->{'RATE'};
	$rain = $ref->{'RAIN_AMOUNT'};
	$today = $ref->{'FALL_TODAY'};
	$yesterday = $ref->{'FALL_YESTERDAY'};
	$tips = $ref->{'TIPS'};
	$time = $ref->{'W_TIME'};
	print &ui_columns_row([
			$rate,
			$rain,
			$today,
			$yesterday,
			$tips,
			$time
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();


ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});