#!/usr/bin/perl
# Write to a manually edited file

require 'eos-lib.pl';
&ReadParseMime();


# Validate input
$in{'data'} =~ s/\r//g;
$in{'data'} =~ /\S/ || &error($text{'manual_edata'});

# Save the file
&open_lock_tempfile(FILE, ">$in{'file'}");
&print_tempfile(FILE, $in{'data'});
&close_tempfile(FILE);


&webmin_log("manual", $in{'file'});

&redirect("index.cgi?mode=report");

