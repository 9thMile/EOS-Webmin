#!/usr/bin/perl

use DBI;


	
require 'eos-lib.pl';
&ReadParse();
ui_print_header(undef, $text{'index_relay'}, "", undef, 1, 1);

$conf = get_eos_config();


#print "Content-type:text/html\r\n\r\n";
print '<html';
print '<head>';
print '<title>Relays</title>';


print &ui_form_start("index.cgi?mode=data");

	@tds = ( undef, undef, "width=10% nowrap" );
	print &ui_columns_start([ $text{'relay_id'},
				  $text{'relay_site'},
				  $text{'relay_script'},
				  $text{'relay_cmd'},
				  $text{'relay_method'},
				  $text{'relay_value'},
				  $text{'relay_op'},
				  $text{'relay_on'},
				  $text{'relay_off'}],
				100, 0, \@tds);

$dbh = DBI->connect('dbi:mysql:weather','weather','eosweather') or die "Connection Error";

#Database items for Identity
$sql = "Select * from RELAYS";
$sth = $dbh->prepare($sql);
$sth->execute() or die "SQL ERROR";
while ($ref = $sth->fetchrow_hashref()) { 
	$id = $ref->{'ID'};
	$site = $ref->{'SITE'};
	$script = $ref->{'SCRIPT'};
	$cmd = $ref->{'CMD'};
	$mtd = $ref->{'METHOD'};
	$val = $ref->{'VALUE'};
	$cmp = $ref->{'COMP'};
	$on = $ref->{'ONSTATE'};
	$off = $ref->{'OFFSTATE'};
	print &ui_columns_row([
			$id,
			$site,
			$script,
			$cmd,
			$mtd,
			$val,
			$cmp,
			$on,
			$off
			], \@tds);

	}



print 'Manage entries in mysql database directly in RELAYS table.</br></br>';
print '</body>';
print '</html>';

$sth->finish();
$dbh->disconnect();

ui_print_footer('index.cgi?mode=data', $text{'index_return_data'});