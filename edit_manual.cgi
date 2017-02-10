#!/usr/bin/perl
# Show form for manually editing php.ini

require 'eos-lib.pl';

&ReadParse();

&ui_print_header("<tt>$in{'file'}</tt>", $text{'manual_title'}, "");

print $text{'manual_desc'},"<p>\n";
print &ui_form_start("save_manual.cgi", "form-data");
print &ui_hidden("file", $in{'file'}),"\n";
print &ui_textarea("data", &read_file_contents($in{'file'}), 40, 88);

print &ui_textbox("file_in", $in{'file'}, 40,1).$text{'Report_Save_As'}.&file_chooser_button("file")." ".&ui_form_end([ [ "save", $text{'Report_Save'} ] ]);

&ui_print_footer("index.cgi?mode=report", $text{'index_return_report'});

