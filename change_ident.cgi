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
		$sth->execute() or die &webmin_log("Update","Station Name to $in{'Station'}","FAILED");
		&webmin_log("Update","Station Name to $in{'Station'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'XTide'}' where LABEL = 'TIDE_STATION'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Tide Station to $in{'XTide'}","FAILED");
		&webmin_log("Update","Tide Station to $in{'XTide'}","Success");

	}

if ($in{'station_loc'}) {

	}
	else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Latitude'}' where LABEL = 'LATITUDE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Latitude change to $in{'Latitude'}","FAILED");
		&webmin_log("Update","Latitude changed to $in{'Latitude'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Longitude'}' where LABEL = 'LONGITUDE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Longitude change to $in{'Longitude'}","FAILED");
		&webmin_log("Update","Longitude changed to $in{'Longitude'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE = $in{'Altitude'} where LABEL = 'ALTITUDE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Altitude change to $in{'Altitude'}","FAILED");
		&webmin_log("Update","Altitude changed to $in{'Altitude'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Address'}' where LABEL = 'ADDRESS'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Address change to $in{'Address'}","FAILED");
		&webmin_log("Update","Address changed to $in{'Address'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'City'}' where LABEL = 'CITY'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","City change to $in{'City'}","FAILED");
		&webmin_log("Update","City changed to $in{'City'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'State'}' where LABEL = 'STATE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","State/Province change to $in{'State'}","FAILED");
		&webmin_log("Update","State/Province changed to $in{'State'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Country'}' where LABEL = 'COUNTRY'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","County/Country change to $in{'Country'}","FAILED");
		&webmin_log("Update","County/Country changed to $in{'Country'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Zip'}' where LABEL = 'ZIP'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Zip/Postal code change to $in{'Zip'}","FAILED");
		&webmin_log("Update","Zip/Postal code changed to $in{'Zip'}","Success");
	}





&redirect("index.cgi?mode=ident");
