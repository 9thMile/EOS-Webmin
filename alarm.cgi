#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_alarm'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS ALARMS</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'Alarm_Type'},
				  $text{'Alarm_Message'},
				  $text{'Alarm_Start'}],
				100, 0, \@tds);


$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from ALARM order by AM_START desc limit 0, 50";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$type = $ref->{'AM_TYPE'};
	$message = $ref->{'MESSAGE'};
	$ams = $ref->{'AM_START'};
	print &ui_columns_row([
			$type,
			$message,
			$ams], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});