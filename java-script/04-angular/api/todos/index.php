<?php

$array = [
    ["text"=> "abc"],
    ["text"=> "def"],
    ["text"=> "ghi"]
];


//header("HTTP/1.1 500 Internal Server Error");
header('Content-type: application/json');

echo json_encode($array);
