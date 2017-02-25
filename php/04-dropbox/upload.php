<?php

# Include the Dropbox SDK libraries
require_once "vendor/autoload.php";
use \Dropbox as dbx;

$dotenv = new Dotenv\Dotenv(__DIR__);
$dotenv->load();
$accessToken = getenv('accessToken');

$dbxClient = new dbx\Client($accessToken, "PHP-Example/1.0");
$accountInfo = $dbxClient->getAccountInfo();
#print_r($accountInfo);

$f = fopen('composer.json', 'rb');
$result = $dbxClient->uploadFile("/composer.json", dbx\WriteMode::add(), $f);
fclose($f);
print_r($result);

