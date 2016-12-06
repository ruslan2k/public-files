var casper = require('casper').create();

casper.start('http://ru0.aptinfo.net:8000/account/signup/', function () {
  this.echo(this.getTitle());
  this.waitForSelector('form[action="/account/signup/"]');
});

casper.then(function () {
  this.fill('form#signup_form', {
    username: 'u1',
    password: 'u1',
    password_confirm: 'u1',
    email: 'u1@aptinfo.net',
  }, true);
});


casper.then(function () {
  this.echo('ok');
  casper.capture('1.png');
});


casper.run();
