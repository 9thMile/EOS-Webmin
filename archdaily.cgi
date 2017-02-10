#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_archdaily'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>EOS Archive Daily</title>';

print &ui_form_start("index.cgi?mode=data");
	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'arch_date'},
				  $text{'arch_temp'},
				  $text{'arch_temp_hi'},
				  $text{'arch_temp_low'},
				  $text{'arch_hum'},
				  $text{'arch_dew'},
				  $text{'arch_wind_speed'},
				  $text{'arch_wind_hi'},
				  $text{'arch_wind_run'},
				  $text{'arch_wind_dir'},
				  $text{'arch_bar'},
				  $text{'arch_rain'},
				  $text{'arch_solar_energy'},
			          $text{'arch_sunhrs'},
				  $text{'arch_heat_dd'},
				  $text{'arch_cool_dd'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from CORE_DATE order by WE_DATE desc limit 0,100";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$date = $ref->{'WE_DATE'};
	$tout = $ref->{'TEMP_AVG'};
	$thi = $ref->{'TEMP_HI'};
	$tlow = $ref->{'TEMP_LOW'};
	$hum = $ref->{'HUM_AVG'};
	$dew = $ref->{'DEW_AVG'};
	$ws = $ref->{'WIND_AVG'};
	$wh = $ref->{'WIND_HI'};
	$wr = $ref->{'WIND_RUN'};
	$wd = $ref->{'WIND_DIR'};
	$bar = $ref->{'BAR'};
	$r = $ref->{'RAIN'};
	$se = $ref->{'SOLAR_ENERGY'};
	$sun = #ref->{'SUN_HRS'};
	$hdd = $ref->{'HEAT_DD'};
	$cdd = $ref->{'COOL_DD'};
	print &ui_columns_row([
			$date,
			$tout,
			$thi,
			$tlow,
			$hum,
			$dew,
			$ws,
			$wh,
			$wr,
			$wd,
			$bar,
			$r,
			$se,
			$sun,
			$hdd,
			$cdd
			], \@tds);

	}



print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();


ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});