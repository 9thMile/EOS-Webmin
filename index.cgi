#!/usr/bin/perl

use DBI;
	
require 'eos-lib.pl';
&ReadParse();
&ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '</head>';
print '<body>';
print '<h2>'.$text{'header'}.'</h2>';
&generate_icon('images/icon.gif',$text{'designed_by'},,'http://9thmile.com',48,48,'','');

print $text{'header_line1'}.'<br>';
print $text{'header_line2'}.'<p><p><p>';

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select STR_VALUE from STATION where LABEL = 'NAME'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$name = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BROKER_ADDRESS'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$b_address = $ref->{'STR_VALUE'};
	}$sql = "Select STR_VALUE from STATION where LABEL = 'BROKER_CLIENT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$b_client = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BROKER_PORT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$b_port = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BROKER_USN'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$b_usn = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BROKER_PWD'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$b_pwd = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'CITY'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$city = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'STATE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$state = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'ADDRESS'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$address = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'COUNTRY'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$country = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'ZIP'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$zip = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'LATITUDE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$lat = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'LONGITUDE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$long = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALTITUDE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$altitude = $ref->{'INT_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'TIDE_STATION'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$xtide = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'COMPASS'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$compass = $ref->{'INT_VALUE'};
	}
$sql = "Select FLOAT_VALUE from STATION where LABEL = 'VARIATION'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$variation = $ref->{'FLOAT_VALUE'};
	}
$sql = "Select FLOAT_VALUE from STATION where LABEL = 'SOLAR_FACTOR'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$solarfactor = $ref->{'FLOAT_VALUE'};
	}
$sql = "Select FLOAT_VALUE from STATION where LABEL = 'HEAT_BASE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$heatbase = $ref->{'FLOAT_VALUE'};
	}
$sql = "Select FLOAT_VALUE from STATION where LABEL = 'COOL_BASE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$coolbase = $ref->{'FLOAT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SUN_TRIGGER'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$sunbase = $ref->{'INT_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'REPORT_BASE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$reportbase = $ref->{'STR_VALUE'};
	}
$sql = "Select DESCRIPT from STATION where LABEL = 'TEMP_NORMAL'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$tempnormal = $ref->{'DESCRIPT'};
	}
$sql = "Select DESCRIPT from STATION where LABEL = 'RAIN_NORMAL'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$rainnormal = $ref->{'DESCRIPT'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'RAIN_TYPE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$def_raintype = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'WIND_AVG'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$def_windavg = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'STAT_ID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$ID = $ref->{'INT_VALUE'};
	}

#database items for Modules
$sql = "Select INT_VALUE from STATION where LABEL = 'UPDATE_ON'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$interval = $ref->{'INT_VALUE'};
	}
$sql = "Select FLOAT_VALUE from STATION where LABEL = 'UPDATE_ON'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$offset = $ref->{'FLOAT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'WAIT_ON'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$wait = $ref->{'INT_VALUE'};
	}

$sql = "Select INT_VALUE, STR_VALUE from STATION where LABEL = 'WIND_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$windcount = $ref->{'INT_VALUE'};
	$windtrigger = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE, STR_VALUE from STATION where LABEL = 'TEMP_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$tempcount = $ref->{'INT_VALUE'};
	$temptrigger = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE, STR_VALUE from STATION where LABEL = 'RAIN_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$raincount = $ref->{'INT_VALUE'};
	$raintrigger = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'PRESSURE_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$pressurecount = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SOLAR_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$solarcount = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SOIL_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$soilcount = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE, FLOAT_VALUE, STR_VALUE from STATION where LABEL = 'DEPTH_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$depthcount = $ref->{'INT_VALUE'};
	$datum = $ref->{'FLOAT_VALUE'};
	$depthtrigger= $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'DEPTH_HHWL'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$hhwl = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'BOARD_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$boardcount = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_VOLTS'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$alarmvolts = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'LOCATION_COUNT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$locationcount = $ref->{'INT_VALUE'};
	}
#database items to retrieve for Pushes
$sql = "Select STR_VALUE from STATION where LABEL = 'USER_KEY'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$userkey = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'APP_TOKEN'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$appkey = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ERROR_LEVEL'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$errorlevel = $ref->{'INT_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'REM_CONN'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$remurl = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'REM_PHP'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$remphp = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BURST_USN'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$burstusn = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BURST_PWD'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$burstpwd = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE, INT_VALUE from STATION where LABEL = 'REM_BURST'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$remburst = $ref->{'STR_VALUE'};
	$remburston = $ref->{'INT_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'REM_ID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$remid = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'PWS_ID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$pwsid = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'PWS_PWD'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$pwspwd = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'WOW_ID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$wowid = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'WOW_KEY'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$wowkey = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'W_UNDER_ID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$underid = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'W_UNDER_API'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$underapi = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'W_UNDER_CAMID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$undercamid = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'W_UNDER_CAMFILE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$undercamfile = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'W_UNDER_PWD'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$underpass = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'AWEKAS_ID'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$awekas = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'WEBCAM_ADDRESS'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$camaddress = $ref->{'STR_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'HAS_FAN'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$fan = $ref->{'INT_VALUE'};
	}

$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_TEMP'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$atemp = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_WIND'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$awind = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_PRESSURE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$apressure = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_SOLAR'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$asolar = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_BOARD'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$aboard = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_RAIN'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$arain = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'ALARM_SOIL'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$asoil = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE, FLOAT_VALUE from STATION where LABEL = 'ALARM_DEPTH'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$adepth = $ref->{'INT_VALUE'};
	$adjdepth = $ref->{'FLOAT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SHOW_HUMIDITY'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$showhumidity = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SHOW_DEWPOINT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$showdewpoint = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SHOW_WINDCHILL'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$showwindchill = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SHOW_COMPASS'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$showcompass = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SHOW_SOLAR'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$showsolar = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'SHOW_ENERGY'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$showenergy = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'USE_GOOGLE'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$usegoogle = $ref->{'INT_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'BG_COLOR'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$bgcolor = $ref->{'STR_VALUE'};
	}
#Database items for NMEA
$sql = "Select INT_VALUE from STATION where LABEL = 'NMEA_ON'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_on = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'NMEA_MDA'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_mda = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'NMEA_MWD'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_mwd = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'NMEA_MWV'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_mwv = $ref->{'INT_VALUE'};
	}
$sql = "Select INT_VALUE from STATION where LABEL = 'NMEA_VWR'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_vwr = $ref->{'INT_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'NMEA_IN_PORT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_inport = $ref->{'STR_VALUE'};
	}
$sql = "Select STR_VALUE from STATION where LABEL = 'NMEA_OUT_PORT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_outport = $ref->{'STR_VALUE'};
	}
$sql = "Select (case when INT_VALUE = 0 then 0 else 1 end) as USE_IN, (case when INT_VALUE = 2 then 1 else 0 end) as USE_OUT from STATION where LABEL = 'NMEA_GGA'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_gga_in = $ref->{'USE_IN'};
	$nmea_gga_out = $ref->{'USE_OUT'};
	}
$sql = "Select (case when INT_VALUE = 0 then 0 else 1 end) as USE_IN, (case when INT_VALUE = 2 then 1 else 0 end) as USE_OUT from STATION where LABEL = 'NMEA_RMC'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_rmc_in = $ref->{'USE_IN'};
	$nmea_rmc_out = $ref->{'USE_OUT'};
	}
$sql = "Select (case when INT_VALUE = 0 then 0 else 1 end) as USE_IN, (case when INT_VALUE = 2 then 1 else 0 end) as USE_OUT from STATION where LABEL = 'NMEA_HDT'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_hdt_in = $ref->{'USE_IN'};
	$nmea_hdt_out = $ref->{'USE_OUT'};
	}
$sql = "Select (case when INT_VALUE = 0 then 0 else 1 end) as USE_IN, (case when INT_VALUE = 2 then 1 else 0 end) as USE_OUT from STATION where LABEL = 'NMEA_HDM'";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$nmea_hdm_in = $ref->{'USE_IN'};
	$nmea_hdm_out = $ref->{'USE_OUT'};
	}

@tabs = ( );
push(@tabs, [ "ident", $text{'index_tabident'}, "index.cgi?mode=ident" ]);
push(@tabs, [ "settings", $text{'index_tabsettings'}, "index.cgi?mode=settings" ]);
push(@tabs, [ "modes", $text{'index_tabmodes'}, "index.cgi?mode=modes" ]);
push(@tabs, [ "nmea", $text{'index_tabnmea'}, "index.cgi?mode=nmes" ]);
push(@tabs, [ "push", $text{'index_tabpush'}, "index.cgi?mode=push" ]);
push(@tabs, [ "data", $text{'index_tabdata'}, "index.cgi?mode=data" ]);
push(@tabs, [ "report", $text{'index_tabreport'}, "index.cgi?mode=report" ]);


print &ui_tabs_start(\@tabs, "mode", $in{'mode'} || $tabs[0]->[0], 1);
print &ui_tabs_start_tab("mode", "ident");
print &ui_form_start("change_ident.cgi","post");

print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_station'},'name'),
		&ui_radio("station_def", 1,
			  [ [ 1, $text{'index_passleave'}."</br>" ],
			    [ 0, $text{'index_passset'} ] ])."</br>".
		&ui_textbox("Station", "$name", 20)." ".
		$text{'index_stationID'}." ".
		&ui_textbox("StationID", "$ID", 5,1)."</br>".
		&ui_textbox("XTide", "$xtide", 20)." ".$text{'index_xtide'});
print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_stationloc'},'location'),
		&ui_radio("station_loc", 1,
			  [ [ 1, $text{'index_passleave'}."</br>" ],
			    [ 0, $text{'index_passset'} ] ])."</br>".
		&ui_textbox("Latitude", "$lat", 14).$text{'index_latitude'}."  ".
		&ui_textbox("Longitude", "$long", 14).$text{'index_longitude'}." ".
		&ui_textbox("Altitude", "$altitude", 3).$text{'index_altitude'}."</br></br>".
		&ui_textbox("Address", "$address", 30).$text{'index_address'}."</br>".
		&ui_textbox("City", "$city", 12).$text{'index_city'}."</br>".
		&ui_textbox("State", "$state", 12).$text{'index_state'}."</br>".
		&ui_textbox("Country", "$country", 12).$text{'index_country'}."  ".
		&ui_textbox("Zip", "$zip", 12).$text{'index_zip'}."<br>");
	
print &ui_table_end();




print &ui_submit($text{'index_ok'});
print &ui_form_end();

print &ui_tabs_end_tab();

print &ui_tabs_start_tab("mode", "settings");

print &ui_form_start("change_settings.cgi","post");

	print &ui_table_start(undef, undef, 2);
		my @mods;
		push(@mods, ['1', '10']);
		print &ui_table_row(hlink($text{'index_rainsensor'},'rainsensor'),
			&ui_radio("station_rain_sensor", 1,
				  [ [ 1, $text{'index_passleave'}." " ],
				    [ 0, $text{'index_r_type'} ] ])." ".
			&ui_select('rain_sensor', $def_raintype, @mods ));
		
	print &ui_table_end();
	
	print &ui_table_start(undef, undef, 2);
		my @mods2;
		push(@mods2, ['1','2','3','4','5' ]);
		print &ui_table_row(hlink($text{'index_windsensor'},'windsensor'),
			&ui_radio("station_wind_sensor", 1,
				  [ [ 1, $text{'index_passleave'}." " ],
				    [ 0, $text{'index_w_sensor'} ] ])." ".
		&ui_select('wind_sensor', $def_windavg, @mods2 ));
	print &ui_table_end();

	print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_normals'},'normals'),
		&ui_radio("station_normals", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("temp", "$tempnormal", 50).$text{'index_tempnormal'}."<br>".
		&ui_textbox("rain", "$rainnormal", 50).$text{'index_rainnormal'});
	
	print &ui_table_end();	
print "</br>";
	print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_base'},'base'),
		&ui_radio("station_base", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("compass", "$compass", 5).$text{'index_compass'}." ".
		&ui_textbox("variation", "$variation", 5).$text{'index_variation'}."</br></br>".		
		&ui_textbox("heat", "$heatbase", 5).$text{'index_heatbase'}." ".
		&ui_textbox("cool", "$coolbase", 5).$text{'index_coolbase'}."</br></br>".
		&ui_textbox("solarf", "$solarfactor", 5).$text{'index_solarfactor'}." ".
		&ui_textbox("sun", "$sunbase", 5).$text{'index_sunbase'});
	
	print &ui_table_end();	
print "</br>";
	print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_report'},'reports'),
		&ui_radio("station_report", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])." ".
		&ui_textbox("reportdir", "$reportbase", 30).$text{'index_reportbase'});
	
	print &ui_table_end();
print "</br>";
	print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_camera'},'camera'),
		&ui_radio("station_camera", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])." ".
		&ui_textbox("camaddress", "$camaddress", 40).$text{'index_camaddress'});
	
	print &ui_table_end();
print &ui_submit($text{'index_ok'});
print &ui_form_end();
print &ui_tabs_end_tab();

print &ui_tabs_start_tab("mode", "modes");
print &ui_form_start("change_mode.cgi","post");

print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_modules'},'modules'),
		&ui_radio("station_mods", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."</br><strong>"
		.$text{'index_modulebase'}."</strong> </br> ".		
		&ui_textbox("Temp", "$tempcount", 5).&ui_checkbox("ATemp",1 , $text{'index_c_temp'},"$atemp")." ".
		&ui_textbox("TempTrigger", "$temptrigger", 30)."</br>".
		&ui_checkbox("Fan_On",1 , $text{'index_fan'},"$fan")."</br>".
		&ui_textbox("Pressure", "$pressurecount", 5).&ui_checkbox("APressure",1 , $text{'index_c_pressure'},"$apressure")."</br><strong>"		
		.$text{'index_modulerain'}."</strong><br>".
		&ui_textbox("Rain", "$raincount", 5).&ui_checkbox("ARain",1 , $text{'index_c_rain'},"$arain").
		&ui_textbox("RainTrigger", "$raintrigger", 30)."</br><strong>"
		.$text{'index_modulewind'}."</strong><br>".
		&ui_textbox("Wind", "$windcount", 5).&ui_checkbox("AWind",1 , $text{'index_c_wind'},"$awind").
		&ui_textbox("WindTrigger", "$windtrigger", 30)."</br><strong>"
		.$text{'index_modulesolar'}."</strong><br>".
		&ui_textbox("Solar", "$solarcount", 5).&ui_checkbox("ASolar",1 , $text{'index_c_solar'},"$asolar")."</br><strong>"
		.$text{'index_modulesoil'}."</strong><br>".
		&ui_textbox("Soil", "$soilcount", 5).&ui_checkbox("ASoil",1 , $text{'index_c_soil'},"$asoil")."</br><strong>"
		.$text{'index_moduledepth'}."</strong><br>".
		&ui_textbox("Depth", "$depthcount", 5).&ui_checkbox("ADepth",1 , $text{'index_c_depth'},"$adepth")." ".
		&ui_textbox("DepthTrigger", "$depthtrigger", 20)."</br>".
		&ui_textbox("AdjDepth", "$adjdepth", 5).&ui_textbox("Datum", "$datum", 5).&ui_textbox("HHWL", "$hhwl", 5)."<strong>".$text{'index_c_depth2'}."</br>".
		$text{'index_moduleother'}."</strong><br>".
		&ui_textbox("Board", "$boardcount", 5).&ui_checkbox("ABoard",1 , $text{'index_c_board'},"$aboard")." ".
		&ui_textbox("Volts", "$alarmvolts", 5).$text{'index_volts'}."<br><strong>".
		&ui_textbox("Location", "$locationcount", 5).$text{'index_c_location'}."</strong>");


print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_instruments'},'instruments'),
		&ui_radio("station_instruments", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("Compass", "$showcompass", 3).$text{'index_i_compass'}."</br> ".
		&ui_checkbox("Humidity",1 , $text{'index_i_humidity'},"$showhumidity")." ".
		&ui_checkbox("DewPoint",1 , $text{'index_i_dewpoint'},"$showdewpoint")."".
		&ui_checkbox("WindChill",1 , $text{'index_i_windchill'},"$showwindchill")."</br>".
		&ui_checkbox("Rad",1 , $text{'index_i_solar'},"$showsolar")." ".
		&ui_checkbox("Eng",1 , $text{'index_i_energy'},"$showenergy")."</br>".
		&ui_textbox("Bcolor", "$bgcolor", 10).$text{'index_i_color'}."</br>".
		&ui_checkbox("Google",1 , $text{'index_i_google'},"$usegoogle"));



print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_archive'},'archive'),
		&ui_radio("station_arch", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passarch'} ] ])."</br>".
		$text{'index_interval'}." ".
		&ui_textbox("Interval", "$interval", 3)." ".
		$text{'index_offset'}." ".
		&ui_textbox("Offset", "$offset", 3)." ".
		$text{'index_wait'}." ".
		&ui_textbox("Wait", "$wait", 3));
	
print &ui_table_end();


print &ui_submit($text{'index_ok'});
print &ui_form_end();


print &ui_tabs_end_tab();

print &ui_tabs_start_tab("mode", "nmea");
print &ui_form_start("change_nmea.cgi","post");
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_nmea'},'nmea'),
		&ui_radio("station_nmea", 1,
			  [ [ 1, $text{'index_passleave'}."<br>" ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("INPORT", "$nmea_inport", 35).$text{'index_nmeain'}."<br>".
		&ui_textbox("OUTPORT", "$nmea_outport", 35).$text{'index_nmeaout'}."<br>".
		&ui_checkbox("NMEA_ON",1 , $text{'index_nmeaon'},"$nmea_on")."<br>".
		$text{'index_nmeaselect'}."<br>".
		&ui_checkbox("NMEA_MDA",1 , $text{'index_nmeamda'},"$nmea_mda")."<br>".
		&ui_checkbox("NMEA_MWD",1 , $text{'index_nmeamwd'},"$nmea_mwd")."<br>".
		&ui_checkbox("NMEA_MWV",1 , $text{'index_nmeamwv'},"$nmea_mwv")."<br>".
		&ui_checkbox("NMEA_VWR",1 , $text{'index_nmeavwr'},"$nmea_vwr")."<br><br>".
		$text{'index_nmeawith'}."<br>".
		&ui_checkbox("NMEA_GGAIN",1 , $text{'index_nmeagga'},"$nmea_gga_in").
		&ui_checkbox("NMEA_GGAOUT",1 , $text{'index_nmea_useout'},"$nmea_gga_out")."<br>".
		&ui_checkbox("NMEA_RMCIN",1 , $text{'index_nmearmc'},"$nmea_rmc_in").
		&ui_checkbox("NMEA_RMCOUT",1 , $text{'index_nmea_useout'},"$nmea_rmc_out")."<br>".
		&ui_checkbox("NMEA_HDTIN",1 , $text{'index_nmeahdt'},"$nmea_hdt_in").
		&ui_checkbox("NMEA_HDTOUT",1 , $text{'index_nmea_useout'},"$nmea_hdt_out")."<br>".
		&ui_checkbox("NMEA_HDMIN",1 , $text{'index_nmeahdm'},"$nmea_hdm_in").
		&ui_checkbox("NMEA_HDMOUT",1 , $text{'index_nmea_useout'},"$nmea_hdm_out"));

print &ui_table_end();
print &ui_submit($text{'index_ok'});
print &ui_form_end();
print &ui_tabs_end_tab();

print &ui_tabs_start_tab("mode", "push");
print &ui_form_start("change_push.cgi","post");
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_pushover'},'pushover'),
		&ui_radio("station_push", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("UserKey", "$userkey", 35).$text{'index_pushuser'}." ".
		&ui_textbox("AppKey", "$appkey", 35).$text{'index_pushkey'});
	
print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_broker'},'broker'),
		&ui_radio("station_broker", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("BrokerAddress", "$b_address", ).$text{'index_brokeraddress'}." ".
		&ui_textbox("BrokerClient", "$b_client", ).$text{'index_brokerclient'}." ".
		&ui_textbox("BrokerPort", "$b_port", 4).$text{'index_brokerport'}."<br>".
		&ui_textbox("BrokerUSN", "$b_usn", 20).$text{'index_brokerusn'}." ".
		&ui_textbox("BrokerPWD", "$b_pwd", 20).$text{'index_brokerpwd'});
	
print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_under'},'wunder'),
		&ui_radio("station_under", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("UnderID", "$underid", 35).$text{'index_underid'}." ".
		&ui_textbox("UnderPass", "$underpass", 35).$text{'index_underpass'}."</br></br>".
		ui_textbox("UnderCAMID", "$undercamid", 35).$text{'index_undercamid'}." ".
		&ui_textbox("UnderCAMFILE", "$undercamfile", 35).$text{'index_undercamfile'}."</br></br>".
		&ui_textbox("UnderAPI", "$underapi", 35).$text{'index_underapi'}."</br></br>".
		&ui_textbox("Awekas", "$awekas", 35).$text{'index_awekas'});
	
print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_remote'},'remote'),
		&ui_radio("station_remote", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("RemURL", "$remurl", 35).$text{'index_remurl'}."<br> ".
		&ui_textbox("RemPHP", "$remphp", 35).$text{'index_remphp'}."<br>".
		&ui_textbox("RemBURST", "$remburst", 35).$text{'index_remburst'}." ".&ui_checkbox("remBURSTON",1 , $text{'index_remburston'},"$remburston")."<br>".
		&ui_textbox("BurstUSN", "$burstusn", 15).$text{'index_burstusn'}." ".&ui_textbox("BurstPWD", "$burstpwd", 15).$text{'index_burstpwd'}."<br>".
		&ui_textbox("RemID", "$remid", 50).$text{'index_remid'});
	
print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_pws'},'pws'),
		&ui_radio("pws_remote", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("PWS_ID", "$pwsid", 20).$text{'index_pwsid'}."<br>".
		&ui_textbox("PWS_PWD", "$pwspwd", 20).$text{'index_pwspwd'});
	
print &ui_table_end();
print "</br>";
print &ui_table_start(undef, undef, 2);

	print &ui_table_row(hlink($text{'index_wow'},'wow'),
		&ui_radio("wow_remote", 1,
			  [ [ 1, $text{'index_passleave'}." " ],
			    [ 0, $text{'index_passset'} ] ])."<br>".
		&ui_textbox("WOW_ID", "$wowid", 20).$text{'index_wowid'}."<br>".
		&ui_textbox("WOW_KEY", "$wowkey", 20).$text{'index_wowkey'});
	
print &ui_table_end();

print &ui_submit($text{'index_ok'});
print &ui_form_end();


print &ui_tabs_end_tab();

print &ui_tabs_start_tab("mode", "report");
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", $reportbase."/noaamo.txt", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_NOAAMO'}</b>\n";
		print &ui_form_end();
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", $reportbase."/noaaprmo.txt", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_NOAAPRMO'}</b>\n";
		print &ui_form_end();
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", $reportbase."/noaayr.txt", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_NOAAYR'}</b>\n";
		print &ui_form_end();
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", $reportbase."/noaapryr.txt", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_NOAAPRYR'}</b>\n";
		print &ui_form_end();
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", $reportbase."/network-monitor.log", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_network'}</b>\n";
		print &ui_form_end();
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", "/var/www/logs/eos.log", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_eoslog'}</b>\n";
		print &ui_form_end();	
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", "/var/www/logs/eor.log", 40)." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_eorlog'}</b>\n";
		print &ui_form_end();	
		print &ui_form_start("edit_manual.cgi");
		print &ui_textbox("file", undef, 40)." ".
		      &file_chooser_button("file")." ".
		      &ui_submit($text{'index_open'})."<b>$text{'index_anyfile'}</b>\n";
		print &ui_form_end();

print &ui_tabs_end_tab();

print &ui_tabs_start_tab("mode", "data");



push(@links, "wind.cgi");
push(@titles, $text{'index_wind'});
push(@icons, "images/wind.gif");
push(@links, "solar.cgi");
push(@titles, $text{'index_solar'});
push(@icons, "images/sunny.gif");
push(@links, "soil.cgi");
push(@titles, $text{'index_soil'});
push(@icons, "images/soil.gif");
push(@links, "rain.cgi");
push(@titles, $text{'index_rain'});
push(@icons, "images/rainy.gif");
push(@links, "temp.cgi");
push(@titles, $text{'index_temp'});
push(@icons, "images/hazy.gif");
push(@links, "press.cgi");
push(@titles, $text{'index_press'});
push(@icons, "images/pressure.gif");
push(@links, "board.cgi");
push(@titles, $text{'index_board'});
push(@icons, "images/nmea.gif");
push(@links, "location.cgi");
push(@titles, $text{'index_location'});
push(@icons, "images/cargoship.gif");
push(@links, "archext.cgi");
push(@titles, $text{'index_archext'});
push(@icons, "images/archive.gif");
push(@links, "archive.cgi");
push(@titles, $text{'index_archive'});
push(@icons, "images/archive.gif");
push(@links, "archdaily.cgi");
push(@titles, $text{'index_archdaily'});
push(@icons, "images/archive.gif");
push(@links, "nmea.cgi");
push(@titles, $text{'index_nmea'});
push(@icons, "images/nmea.gif");
push(@links, "alarm.cgi");
push(@titles, $text{'index_alarm'});
push(@icons, "images/w-s-warning.gif");
push(@links, "almanac.cgi");
push(@titles, $text{'index_almanac'});
push(@icons, "images/moon.gif");
push(@links, "tide.cgi");
push(@titles, $text{'index_tide'});
push(@icons, "images/table.gif");
&icons_table(\@links, \@titles, \@icons, 4);



	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'feed_type'},
				  $text{'feed_isdone'},
				  $text{'feed_sentence'},
				  $text{'feed_time'}],
				100, 0, \@tds);

$sql = "Select * from FEED order by W_TIME desc limit 0,25";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$type = $ref->{'TYPE'};
	$done = $ref->{'IS_DONE'};
	$sent = $ref->{'SENTENCE'};
	$time = $ref->{'W_TIME'};
	print &ui_columns_row([
			$type,
			$done,
			$sent,
			$time
			], \@tds);

	}
		print "<p>\n";


print &ui_tabs_end_tab();




print &ui_tabs_end(1);

print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();
&webmin_log("Login","EOS","Main page","Displayed");
&ui_print_footer("/", $text{'index'});
