#!/usr/bin/perl

use strict;
use warnings;

use Template;

my $tt = Template->new({
    INCLUDE_PATH => '.',
    INTERPOLATE  => 1,
}) || die "$Template::ERROR\n";

my $vars = {
    name => 'Ruslan',
    debt => 100500,
    hosts => [
        {name => 'app1'},
        {name => 'app2'},        
    ],
};

$tt->process('index.tmpl', $vars, 'index.html') || die $tt->error(), "\n";


