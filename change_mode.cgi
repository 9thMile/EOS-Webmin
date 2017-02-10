#!/usr/bin/perl

use DBI;

require 'eos-lib.pl';
$conf = get_eos_config();
our (%text, %in, %gconfig);
&ReadParse();
$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

if ($in{'station_mods'}) {

		}
		else {
		if ($in{'Fan_On'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'HAS_FAN'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'HAS_FAN'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Has Fan change to $in{'Fan_On'}","FAILED");
		&webmin_log("Update","Has Fan changed to $in{'Fan_On'}","Success");

		if ($in{'ATemp'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_TEMP'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_TEMP'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm temp change to $in{'ATemp'}","FAILED");
		&webmin_log("Update","Alarm temp changed to $in{'ATemp'}","Success");


		if ($in{'AWind'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_WIND'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_WIND'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm wind change to $in{'AWind'}","FAILED");
		&webmin_log("Update","Alarm wind changed to $in{'AWind'}","Success");


		if ($in{'APressure'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_PRESSURE'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_PRESSURE'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm pressure change to $in{'APressure'}","FAILED");
		&webmin_log("Update","Alarm pressure changed to $in{'APressure'}","Success");


		if ($in{'ARain'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_RAIN'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_RAIN'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm rain change to $in{'ARain'}","FAILED");
		&webmin_log("Update","Alarm rain changed to $in{'ARain'}","Success");


		if ($in{'ASolar'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_SOLAR'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_SOLAR'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm solar change to $in{'ASolar'}","FAILED");
		&webmin_log("Update","Alarm solar changed to $in{'ASolar'}","Success");


		if ($in{'ASoil'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_SOIL'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_SOIL'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm soil change to $in{'ASoil'}","FAILED");
		&webmin_log("Update","Alarm soil changed to $in{'ASoil'}","Success");

		if ($in{'ADepth'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1, FLOAT_VALUE = $in{'AdjDepth'} where LABEL = 'ALARM_DEPTH'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0, FLOAT_VALUE = $in{'AdjDepth'} where LABEL = 'ALARM_DEPTH'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm depth change to $in{'ADepth'}","FAILED");
		&webmin_log("Update","Alarm depth changed to $in{'ADepth'}","Success");


		if ($in{'ABoard'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'ALARM_BOARD'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'ALARM_BOARD'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Alarm board change to $in{'ABoard'}","FAILED");
		&webmin_log("Update","Alarm board changed to $in{'ABoard'}","Success");

		$sql = "UPDATE STATION SET INT_VALUE = $in{'Wind'}, STR_VALUE = '$in{'WindTrigger'}'  where LABEL = 'WIND_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Wind Count changed","FAILED");
		&webmin_log("Update","Wind Count changed","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Temp'}, STR_VALUE = '$in{'TempTrigger'}' where LABEL = 'TEMP_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Temp Count changed","FAILED");
		&webmin_log("Update","Temp Count changed","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Rain'}, STR_VALUE = '$in{'RainTrigger'}' where LABEL = 'RAIN_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die  &webmin_log("Update","Rain Count changed","FAILED");
		&webmin_log("Update","Rain Count changed","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Pressure'} where LABEL = 'PRESSURE_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Pressure Count changed to $in{'Pressure'}","FAILED");
		&webmin_log("Update","Pressure Count changed to $in{'Pressure'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Solar'} where LABEL = 'SOLAR_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Solar Count changed to $in{'Solar'}","FAILED");
		&webmin_log("Update","Solar Count changed to $in{'Solar'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Soil'} where LABEL = 'SOIL_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Soil Count changed to $in{'Soil'}","FAILED");
		&webmin_log("Update","Soil Count changed to $in{'Soil'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Depth'}, STR_VALUE = '$in{'DepthTrigger'}', FLOAT_VALUE = '$in{'Datum'}'  where LABEL = 'DEPTH_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Depth Count changed to $in{'Depth'}","FAILED");
		&webmin_log("Update","Depth Count changed to $in{'Depth'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Board'} where LABEL = 'BOARD_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Board Count changed to $in{'Board'}","FAILED");
		&webmin_log("Update","Board Count changed to $in{'Board'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'HHWL'} where LABEL = 'DEPTH_HHWL'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","HHWL changed to $in{'HHWL'}","FAILED");
		&webmin_log("Update","HHWL changed to $in{'HHWL'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Location'} where LABEL = 'LOCATION_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Location Count changed to $in{'Location'}","FAILED");
		&webmin_log("Update","Location Count changed to $in{'Location'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Volts'} where LABEL = 'ALARM_VOLTS'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Volts trigger changed to $in{'Volts'}","FAILED");
		&webmin_log("Update","Volts trigger changed to $in{'Volts'}","Success");
		}
if ($in{'station_arch'}) {

		}
		else {
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Interval'} where LABEL = 'UPDATE_ON'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Archive Interval changed to $in{'Interval'}","FAILED");
		&webmin_log("Update","Archive Interval changed to $in{'Interval'}","Success");
		$sql = "UPDATE STATION SET FLOAT_VALUE = $in{'Offset'} where LABEL = 'UPDATE_ON'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Archive offset changed to $in{'Offset'}","FAILED");
		&webmin_log("Update","Archive Offset changed to $in{'Offset'}","Success");

		$sql = "UPDATE STATION SET INT_VALUE = $in{'Wait'} where LABEL = 'WAIT_ON'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Pause Interval changed to $in{'Wait'}","FAILED");
		&webmin_log("Update","Pause Interval changed to $in{'Wait'}","Success");
		}
if ($in{'station_instruments'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Bcolor'}' where LABEL = 'BG_COLOR'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Background color change to $in{'Bcolor'}","FAILED");
		&webmin_log("Update","Background color changed to $in{'Bcolor'}","Success");

		if ($in{'Humidity'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'SHOW_HUMIDITY'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'SHOW_HUMIDITY'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Humidity changed to $in{'Humidity'}","FAILED");
		&webmin_log("Update","Humidity changed to $in{'Humidity'}","Success");
		if ($in{'DewPoint'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'SHOW_DEWPOINT'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'SHOW_DEWPOINT'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Dew Point changed to $in{'DewPoint'}","FAILED");
		&webmin_log("Update","Dew Point changed to $in{'DewPoint'}","Success");
		if ($in{'WindChill'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'SHOW_WINDCHILL'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'SHOW_WINDCHILL'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Wind Chill changed to $in{'WindChill'}","FAILED");
		&webmin_log("Update","Wind Chill changed to $in{'WindChill'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Compass'} where LABEL = 'SHOW_COMPASS'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Compass Mode changed to $in{'Compass'}","FAILED");
		&webmin_log("Update","Compass Mode changed to $in{'Compass'}","Success");
		if ($in{'Rad'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'SHOW_SOLAR'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'SHOW_SOLAR'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Solar Mode changed to $in{'Rad'}","FAILED");
		&webmin_log("Update","Solar Mode changed to $in{'Rad'}","Success");
		if ($in{'Eng'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'SHOW_ENERGY'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'SHOW_ENERGY'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Energy Mode changed to $in{'Eng'}","FAILED");
		&webmin_log("Update","Energy Mode changed to $in{'Eng'}","Success");
		if ($in{'Google'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'USE_GOOGLE'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'USE_GOOGLE'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Google Mode changed to $in{'Google'}","FAILED");
		&webmin_log("Update","Google Mode changed to $in{'Google'}","Success");
		}
&redirect("index.cgi?mode=modes");
