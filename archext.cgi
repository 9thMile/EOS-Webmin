#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_archext'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Arch Extent</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'extent_tips'},
				  $text{'extent_lat'},
				  $text{'extent_long'},
				  $text{'extent_cog'},
				  $text{'extent_sog'},
				  $text{'extent_volt_s'},
				  $text{'extent_volt_b'},
				  $text{'extent_temp'},
				  $text{'extent_date'},
				  $text{'extent_time'},
				  $text{'extent_datetime'}],
				100, 0, \@tds);


$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from CORE_EXT order by WE_DATE_TIME desc limit 0, 100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$tips = $ref->{'TIPS'};
	$lat = $ref->{'LATITUDE'};
	$long = $ref->{'LONGITUDE'};
	$cog = $ref->{'COG'};
	$sog = $ref->{'SOG'};
	$vhi = $ref->{'VOLTS_S'};
	$vlow = $ref->{'VOLTS_B'};
	$temp = $ref->{'TEMP_BOARD'};
	$wdate = $ref->{'WE_Date'};
	$wtime = $ref->{'WE_Time'};
	$utc = $ref->{'WE_DATE_TIME'};
	print &ui_columns_row([
			$tips,
			$lat,
			$long,
			$cog,
			$sog,
			$vhi,
			$vlow,
			$temp,
			$wdate,
			$wtime,
			$utc
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});