#!/usr/bin/perl

use DBI;

require 'eos-lib.pl';
$conf = get_eos_config();
our (%text, %in, %gconfig);
&ReadParse();
$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

if ($in{'station_nmea'}) {

	}
	else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'INPORT'}' where LABEL = 'NMEA_IN_PORT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA In Port change to $in{'INPORT'}","FAILED");
		&webmin_log("Update","NMEA In Port changed to $in{'INPORT'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'OUTPORT'}' where LABEL = 'NMEA_OUT_PORT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA Out Port change to $in{'OUTPORT'}","FAILED");
		&webmin_log("Update","NMEA Out Port changed to $in{'OUTPORT'}","Success");


		if ($in{'NMEA_ON'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_ON'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_ON'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA ON change to $in{'NMEA_ON'}","FAILED");
		&webmin_log("Update","NMEA ON changed to $in{'NMEA_ON'}","Success");

		if ($in{'NMEA_MDA'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_MDA'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_MDA'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA MDA change to $in{'NMEA_MDA'}","FAILED");
		&webmin_log("Update","NMEA MDA changed to $in{'NMEA_MDA'}","Success");

		if ($in{'NMEA_MWD'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_MWD'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_MWD'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA MWD change to $in{'NMEA_MWD'}","FAILED");
		&webmin_log("Update","NMEA MWD changed to $in{'NMEA_MWD'}","Success");

		if ($in{'NMEA_MWV'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_MWV'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_MWV'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA MWV change to $in{'NMEA_MWV'}","FAILED");
		&webmin_log("Update","NMEA MWV changed to $in{'NMEA_MWV'}","Success");

		if ($in{'NMEA_VWR'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_VWR'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_VWR'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA VWR change to $in{'NMEA_VWR'}","FAILED");
		&webmin_log("Update","NMEA VWR changed to $in{'NMEA_VWR'}","Success");


		if ($in{'NMEA_GGAOUT'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 2 where LABEL = 'NMEA_GGA'";
		} 
		elsif ($in{'NMEA_GGAIN'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_GGA'";
		}
		else {
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_GGA'";
		}

		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA GGA change","FAILED");
		&webmin_log("Update","NMEA GGA changed","Success");

		if ($in{'NMEA_RMCOUT'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 2 where LABEL = 'NMEA_RMC'";
		}
		elsif ($in{'NMEA_RMCIN'} == 1) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_RMC'";
		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_RMC'";}

		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA RMC change","FAILED");
		&webmin_log("Update","NMEA RMC changed","Success");

		if ($in{'NMEA_HDTOUT'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 2 where LABEL = 'NMEA_HDT'";

		}elsif ($in{'NMEA_HDTIN'} ==1) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_HDT'";

		}else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_HDT'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA HDT change","FAILED");
		&webmin_log("Update","NMEA GSV changed","Success");

		if ($in{'NMEA_HDMOUT'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 2 where LABEL = 'NMEA_HDM'";

		}elsif ($in{'NMEA_HDMIN'} ==1) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'NMEA_HDM'";

		}else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'NMEA_HDM'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","NMEA GSV change","FAILED");
		&webmin_log("Update","NMEA GSV changed","Success");

	}




&redirect("index.cgi?mode=nmea");
