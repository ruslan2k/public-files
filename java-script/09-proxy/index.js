const express = require('express')
const request = require('request')
const app = express()

console.log('Promise', typeof Promise);

app.get('/*', (req, res, next) => {
  var newUrl = req.url.replace(/^\//, '');
  console.log(newUrl)
  request(newUrl, function (error, response, body) {
    if (error) {
      console.log(error);
      return res.status(500).send('Error');
    }
    res.header('Access-Control-Allow-Origin', '*');
    //res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    res.send(body)
    //return res.json({'url': req.url, 'path': req.path, 'u': url})
  })
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))

