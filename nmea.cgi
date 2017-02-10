#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_nmea'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS NMEA</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ 'RECID',
				  $text{'nmea_date_time'},
				  $text{'nmea_type'},
					'B1',
					'B2',
					'B3',
					'B4',
					'B5',
					'B6',
					'B7',
					'B8',
					'B9',
					'B10',
					'B11',
					'B12',
					'B13',
					'B14',
					'B15',
					'B16',
					'B17',
					'B18',
					'B19',
					'B20',
				  $text{'nmea_sum'}],

				100, 0, \@tds);


$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from NMEA order by We_Date_Time desc";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$recid = $ref->{'RECID'};
	$date = $ref->{'WE_Date_Time'};
	$type = $ref->{'SENTENCE'};
	$b1 = $ref->{'B1'};
	$b2 = $ref->{'B2'};
	$b3 = $ref->{'B3'};
	$b4 = $ref->{'B4'};
	$b5 = $ref->{'B5'};
	$b6 = $ref->{'B6'};
	$b7 = $ref->{'B7'};
	$b8 = $ref->{'B8'};
	$b9 = $ref->{'B9'};
	$b10 = $ref->{'B10'};
	$b11 = $ref->{'B11'};
	$b12 = $ref->{'B12'};
	$b13 = $ref->{'B13'};
	$b14 = $ref->{'B14'};
	$b15 = $ref->{'B15'};
	$b16 = $ref->{'B16'};
	$b17 = $ref->{'B17'};
	$b18 = $ref->{'B18'};
	$b19 = $ref->{'B19'};
	$bsum = $ref->{'CSUM'};
	print &ui_columns_row([
			$recid,
			$date,
			$type,
			$b1,
			$b2,
			$b3,
			$b4,
			$b5,
			$b6,
			$b7,
			$b8,
			$b9,
			$b10,
			$b11,
			$b12,
			$b13,
			$b14,
			$b15,
			$b16,
			$b17,
			$b18,
			$b19,
			$b20,
			$bsum
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});