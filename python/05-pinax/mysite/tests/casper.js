// Returns a random integer between min (included) and max (excluded) 
// Using Math.round() will give you a non-uniform distribution! 
function getRandomInt(min, max) { 
    return Math.floor(Math.random() * (max - min)) + min; 
}

//Run it
getRandomInt(500000, 1200000);

var casper = require('casper').create();

casper.start('http://ru0.aptinfo.net:8000/account/signup/', function () {
  this.waitForSelector('form[action="/account/signup/"]');
  this.echo(this.getTitle());
});

casper.then(function () {
  var i = getRandomInt(10, 99);
  this.fill('form#signup_form', {
    username: 'u' + i,
    password: '3to4sJvn_MdmOL',
    password_confirm: '3to4sJvn_MdmOL',
    email: 'u'+ i +'@aptinfo.net',
  }, true);
});


casper.then(function () {
  this.echo('ok');
  // casper.capture('1.png');
});


casper.run();
