var express = require('express');
var app = express();
var path = require('path');
var port = process.env.PORT || 8008;

//app.use(express.static('js'));
['/js', '/node_modules'].forEach(function (dir) {
  app.use(dir, express.static(__dirname + dir));
});

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});


console.log('http://localhost:'+ port);

app.listen(port);
