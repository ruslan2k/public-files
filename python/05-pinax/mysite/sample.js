
var casper = require('casper').create();
var login_url = 'http://localhost:8000/account/login/';

casper.start(login_url);

casper.then( function () {
  this.echo('First Page: ' + this.getTitle());
  this.fill('form#singup_form', {
    'username': 'random',
    'password': 'random',
    'password_confirm': 'random',
    'email': 'user@example.com',
  }, true);
});

casper.then( function () {
  this.evaluateOrDie(function () {
    return false;
  }, 'failed');

});

casper.run();
