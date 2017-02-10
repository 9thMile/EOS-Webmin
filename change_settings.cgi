#!/usr/bin/perl

use DBI;

require 'eos-lib.pl';
$conf = get_eos_config();
our (%text, %in, %gconfig);
&ReadParse();
$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

if ($in{'station_normals'}) {

	}
	else {
		$sql = "UPDATE STATION SET DESCRIPT ='$in{'temp'}' where LABEL = 'TEMP_NORMAL'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Temp normals change to $in{'tempnormal'}","FAILED");
		&webmin_log("Update","Temp normals changed to $in{'temp'}","Success");
		$sql = "UPDATE STATION SET DESCRIPT ='$in{'rain'}' where LABEL = 'RAIN_NORMAL'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Rain normals change to $in{'rainnormal'}","FAILED");
		&webmin_log("Update","Rain normals changed to $in{'rain'}","Success");
	}

if ($in{'station_base'}) {

	}
	else {

		$sql = "UPDATE STATION SET INT_VALUE =$in{'heat'}, FLOAT_VALUE = $in{'heat'} where LABEL = 'HEAT_BASE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Heat Base change to $in{'heat'}","FAILED");
		&webmin_log("Update","Heat Base changed to $in{'heat'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE =$in{'cool'}, FLOAT_VALUE = $in{'cool'} where LABEL = 'COOL_BASE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Cool Base change to $in{'cool'}","FAILED");
		&webmin_log("Update","Cool Base changed to $in{'cool'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE =$in{'compass'} where LABEL = 'COMPASS'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Compass change to $in{'compass'}","FAILED");
		&webmin_log("Update","Compass changed to $in{'compass'}","Success");
		$sql = "UPDATE STATION SET FLOAT_VALUE =$in{'variation'} where LABEL = 'VARIATION'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Compass variation change to $in{'variation'}","FAILED");
		&webmin_log("Update","Compass variation changed to $in{'variation'}","Success");
		$sql = "UPDATE STATION SET FLOAT_VALUE =$in{'solarf'} where LABEL = 'SOLAR_FACTOR'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Solar factor change to $in{'solarf'}","FAILED");
		&webmin_log("Update","Solar factor changed to $in{'solarf'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE =$in{'sun'} where LABEL = 'SUN_TRIGGER'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Sun trigger change to $in{'sun'}","FAILED");
		&webmin_log("Update","Sun trigger changed to $in{'sun'}","Success");

	}
if ($in{'station_report'}) {

	}
	else {
		$sql = "UPDATE STATION SET STR_VALUE = '$in{'reportdir'}' where LABEL = 'REPORT_BASE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Report Directory change to $in{'reportdir'}","FAILED");
		&webmin_log("Update","Report Directory changed to $in{'reportdir'}","Success");

	}
if ($in{'station_camera'}) {

	}
	else {
		$sql = "UPDATE STATION SET STR_VALUE = '$in{'camaddress'}' where LABEL = 'WEBCAM_ADDRESS'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Webcam address change to $in{'camaddress'}","FAILED");
		&webmin_log("Update","Webcam address changed to $in{'camaddress'}","Success");

	}
if ($in{'station_rain_sensor'}) {

	}
	else {

		$sql = "UPDATE STATION SET INT_VALUE =$in{'rain_sensor'} where LABEL = 'RAIN_TYPE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Rain Sensor changed to $in{'rain_sensor'}","FAILED");
		&webmin_log("Update","Rain Sensor changed to $in{'rain_sensor'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'DO_UPDATE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Board Update","FAILED");
		&webmin_log("Update","Board Update","Success");


	}

if ($in{'station_wind_sensor'}) {

	}
	else {
		$sql = "UPDATE STATION SET INT_VALUE = $in{'wind_sensor'} where LABEL = 'WIND_AVG'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Wind Sensor changed to $in{'wind_sensor'}","FAILED");
		&webmin_log("Update","Wind Sensor changed to $in{'wind_sensor'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'DO_UPDATE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Board Update","FAILED");
		&webmin_log("Update","Board Update","Success");
	}



&redirect("index.cgi?mode=settings");
