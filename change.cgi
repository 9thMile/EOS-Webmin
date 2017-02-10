#!/usr/bin/perl

use DBI;

require 'eos-lib.pl';
$conf = get_eos_config();
our (%text, %in, %gconfig);
&ReadParse();
$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

if ($in{'station_def'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Station'}' where LABEL = 'NAME'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'StationID'} where LABEL = 'STAT_ID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		}
if ($in{'station_loc'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Latitude'}' where LABEL = 'LATITUDE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Longitude'}' where LABEL = 'LONGITUDE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Altitude'} where LABEL = 'ALTITUDE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		}
if ($in{'station_mods'}) {

		}
		else {
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Wind'} where LABEL = 'WIND_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Temp'} where LABEL = 'TEMP_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Rain'} where LABEL = 'RAIN_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Pressure'} where LABEL = 'PRESSURE_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Solar'} where LABEL = 'SOLAR_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Board'} where LABEL = 'BOARD_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Location'} where LABEL = 'LOCATION_COUNT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		}
if ($in{'station_arch'}) {

		}
		else {
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Interval'} where LABEL = 'UPDATE_ON'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Wait'} where LABEL = 'WAIT_ON'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die "SQL ERROR";
		}

&redirect("index.cgi");
