var casper = require('casper').create();

casper.start('http://ru0.aptinfo.net:8000/account/signup/', function () {
  this.waitForSelector('form[action="/account/signup/"]');
  this.echo(this.getTitle());
});

casper.then(function () {
  this.fill('form#signup_form', {
    username: 'u1',
    password: '3to4sJvn_MdmOL',
    password_confirm: '3to4sJvn_MdmOL',
    email: 'u1@aptinfo.net',
  }, true);
});


casper.then(function () {
  this.echo('ok');
  // casper.capture('1.png');
});


casper.run();
