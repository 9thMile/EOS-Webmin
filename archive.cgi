#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_archive'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Press</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'arch_local_time'},
				  $text{'arch_temp'},
				  $text{'arch_temp_hi'},
				  $text{'arch_temp_low'},
				  $text{'arch_dew'},
				  $text{'arch_wind_chill'},
				  $text{'arch_hum'},
				  $text{'arch_wind_speed'},
				  $text{'arch_wind_hi'},
				  $text{'arch_wind_run'},
				  $text{'arch_wind_dir'},
				  $text{'arch_bar'},
				  $text{'arch_rain'},
				  $text{'arch_rain_rate'},
				  $text{'arch_heat_dd'},
				  $text{'arch_cool_dd'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from CORE_DATA order by WE_DATE_TIME desc limit 0,100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$time = $ref->{'WE_Time'};
	$tout = $ref->{'TEMP_OUT'};
	$thi = $ref->{'TEMP_HI'};
	$tlow = $ref->{'TEMP_LOW'};
	$dew = $ref->{'DEW_OUT'};
	$wc = $ref->{'WIND_CHILL'};
	$hum = $ref->{'HUM_OUT'};
	$ws = $ref->{'WIND_SPEED'};
	$wh = $ref->{'WIND_HI'};
	$wr = $ref->{'WIND_RUN'};
	$wd = $ref->{'WIND_DIR'};
	$bar = $ref->{'BAR'};
	$r = $ref->{'RAIN'};
	$rr = $ref->{'RAIN_RATE'};
	$hdd = $ref->{'HEAT_DD'};
	$cdd = $ref->{'COOL_DD'};
	print &ui_columns_row([
			$time,
			$tout,
			$thi,
			$tlow,
			$dew,
			$wc,
			$hum,
			$ws,
			$wh,
			$wr,
			$wd,
			$bar,
			$r,
			$rr,
			$hdd,
			$cdd
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();


ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});