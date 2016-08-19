var express = require('express');
var app = express();
var path = require('path');

app.git('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

all.listen(8008);
