var express = require('express');
var app = express();
var path = require('path');
var port = process.env.PORT || 8008;

var items = [
  {text: "a"},
  {text: "b"},
  {text: "c"},
];

['/js', '/node_modules'].forEach(function (dir) {
  app.use(dir, express.static(__dirname + dir));
});

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/api/items', function (req, res) {
  res.json(items);
});

console.log('http://localhost:'+ port);

app.listen(port);
