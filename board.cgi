#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_board'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Board</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'board_station'},
				  $text{'board_type'},
				  $text{'board_version'},
				  $text{'board_svoltage'},
				  $text{'board_bvoltage'},
				  $text{'board_temp'},
				  $text{'board_error'},
				  $text{'board_time'}],
				100, 0, \@tds);


$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from BOARD order by W_TIME desc limit 0, 100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$station = $ref->{'STATION'};
	$type = $ref->{'TYPE'};
	$version = $ref->{'VERSION'};
	$svoltage = $ref->{'S_VOLTAGE'};
	$bvoltage = $ref->{'B_VOLTAGE'};
	$temp = $ref->{'C_TEMP'};
	$error = $ref->{'ERROR'};
	$time = $ref->{'W_TIME'};
	print &ui_columns_row([
			$station,
			$type,
			$version,
			$svoltage,
			$bvoltage,
			$temp,
			$error,
			$time
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});