#!/usr/bin/perl

use DBI;

require 'eos-lib.pl';
$conf = get_eos_config();
our (%text, %in, %gconfig);
&ReadParse();
$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";


if ($in{'station_push'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'UserKey'}' where LABEL = 'USER_KEY'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","User Key changed to $in{'UserKey'}","FAILED");
		&webmin_log("Update","User Key changed to $in{'UserKey'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'AppKey'}' where LABEL = 'APP_TOKEN'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Application Key changed to $in{'AppKey'}","FAILED");
		&webmin_log("Update","Application Key changed to $in{'AppKey'}","Success");
		$sql = "UPDATE STATION SET INT_VALUE ='$in{'ErrorLevel'}' where LABEL = 'ERROR_LEVEL'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Error Level changed to $in{'ErrorLevel'}","FAILED");
		&webmin_log("Update","Error Level changed to $in{'ErrorLevel'}","Success");
		}
if ($in{'station_broker'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BrokerAddress'}' where LABEL = 'BROKER_ADRESS'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Broker Address changed to $in{'BrokerAddress'}","FAILED");
		&webmin_log("Update","Broker Address changed to $in{'BrokerAddress'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BrokerClient'}' where LABEL = 'BROKER_CLIENT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Broker Client changed to $in{'BrokerClient'}","FAILED");
		&webmin_log("Update","Broker Client changed to $in{'BrokerClient'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BrokerPort'}' where LABEL = 'BROKER_PORT'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Broker Port changed to $in{'BrokerPort'}","FAILED");
		&webmin_log("Update","Broker Port changed to $in{'BrokerPort'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BrokerUSN'}' where LABEL = 'BROKER_USN'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Broker Username changed to $in{'BrokerUSN'}","FAILED");
		&webmin_log("Update","Broker Username changed to $in{'BrokerUSN'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BrokerPWD'}' where LABEL = 'BROKER_PWD'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Broker password changed to $in{'BrokerPWD'}","FAILED");
		&webmin_log("Update","Broker password changed to $in{'BrokerPWD'}","Success");
		}
if ($in{'station_under'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'UnderID'}' where LABEL = 'W_UNDER_ID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WeatherUnderGround ID change to $in{'UnderID'}","FAILED");
		&webmin_log("Update","WeatherUnderGround ID changed to $in{'UnderID'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'UnderPass'}' where LABEL = 'W_UNDER_PWD'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WeatherUnderGround Password change to *****","FAILED");
		&webmin_log("Update","WeatherUnderGround Password changed to *****","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'UnderAPI'}' where LABEL = 'W_UNDER_API'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WeatherUnderGround API Key change to *****","FAILED");
		&webmin_log("Update","WeatherUnderGround API Key changed to *****","Success");

		$sql = "UPDATE STATION SET STR_VALUE ='$in{'UnderCAMID'}' where LABEL = 'W_UNDER_CAMID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WeatherUnderGround CAM ID change to $in{'UnderCAMID'}","FAILED");
		&webmin_log("Update","WeatherUnderGround CAM ID changed to $in{'UnderCAMID'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'UnderCAMFILE'}' where LABEL = 'W_UNDER_CAMFILE'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WeatherUnderGround Cam file change to $in{'UnderCAMFILE'}","FAILED");
		&webmin_log("Update","WeatherUnderGround Cam file changed to $in{'UnderCAMFILE'}","Success");

		$sql = "UPDATE STATION SET STR_VALUE ='$in{'Awekas'}' where LABEL = 'AWEKAS_ID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Awekas ID change to *****","FAILED");
		&webmin_log("Update","Awekas ID changed to *****","Success");

		}
if ($in{'station_remote'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'RemURL'}' where LABEL = 'REM_CONN'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Remote URL changed to $in{'RemURL'}","FAILED");
		webmin_log("Update","Remote URL changed to $in{'RemURL'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'RemPHP'}' where LABEL = 'REM_PHP'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Remote PHP changed to $in{'RemPHP'}","FAILED");
		&webmin_log("Update","Remote PHP changed to $in{'RemPHP'}","Success");

		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BurstUSN'}' where LABEL = 'BURST_USN'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","FTP Username changed to $in{'BurstUSN'}","FAILED");
		&webmin_log("Update","Burst Username changed to $in{'BurstUSN'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'BurstPWD'}' where LABEL = 'BURST_PWD'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","FTP password changed to $in{'BurstPWD'}","FAILED");
		&webmin_log("Update","FTP password changed to $in{'BurstPWD'}","Success");
		
		if ($in{'remBURSTON'} ==1 ) {
		$sql = "UPDATE STATION SET INT_VALUE = 1 where LABEL = 'REM_BURST'";

		}
		else{
		$sql = "UPDATE STATION SET INT_VALUE = 0 where LABEL = 'REM_BURST'";}
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","BURST ON change to $in{'remBURSTON'}","FAILED");
		&webmin_log("Update","BURST ON changed to $in{'remBURSTON'}","Success");

		$sql = "UPDATE STATION SET STR_VALUE ='$in{'RemBURST'}' where LABEL = 'REM_BURST'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Remote Burst changed to $in{'RemBURST'}","FAILED");
		&webmin_log("Update","Remote BURST changed to $in{'RemBURST'}","Success");
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'RemID'}' where LABEL = 'REM_ID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","Remote RemID changed to $in{'RemID'}","FAILED");
		&webmin_log("Update","Remote RemID changed to $in{'RemID'}","Success");
		}

if ($in{'station_pws'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'PWS_ID'}' where LABEL = 'PWS_ID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","PWS Id changed to $in{'PWS_ID'}","FAILED");
		webmin_log("Update","PWS Id changed to $in{'RemURL'}","Success");

		$sql = "UPDATE STATION SET STR_VALUE ='$in{'PWS_PWD'}' where LABEL = 'PWS_PWD'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","PWS Password changed to $in{'PWS_PWD'}","FAILED");
		&webmin_log("Update","PWS Password changed to $in{'PWS_PWD'}","Success");
		}

if ($in{'station_wow'}) {

		}
		else {
		$sql = "UPDATE STATION SET STR_VALUE ='$in{'WOW_ID'}' where LABEL = 'WOW_ID'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WOW Id changed to $in{'WOW_ID'}","FAILED");
		webmin_log("Update","Remote URL changed to $in{'RemURL'}","Success");

		$sql = "UPDATE STATION SET STR_VALUE ='$in{'WOW_KEY'}' where LABEL = 'WOW_KEY'";
		$sth = $dbh->prepare($sql);
		$sth->execute() or die &webmin_log("Update","WOW Key changed to $in{'WOW_KEY'}","FAILED");
		&webmin_log("Update","WOW Key changed to $in{'WOW_KEY'}","Success");
		}

&redirect("index.cgi?mode=push");
