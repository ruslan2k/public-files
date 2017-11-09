const express = require('express')
const app = express()

app.all('/*', (req, res) => {
  //return res.send('Hello World', req.query)
  return res.json({'url': req.url})
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))




