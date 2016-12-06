var casper = require('casper').create();

casper.start('http://ru0.aptinfo.net:8000/account/signup/', function () {
  this.echo(this.getTitle());
});

casper.waitForSelector("form", function () {
  this.fill('form#singup_form', {
    'input[name=username]': 'u1',
    'input[name=password]': 'u1',
    'input[name=password_confirm]': 'u1',
    'input[name=email]': 'u1@aptinfo.net',
  }, true);
});


// casper.open('http://localhost:8000/account/signup/', {
//   method: 'post',
//   date: {
//     username: 'u1',
//     password: 'p1',
//     password_confirm: 'p1',
//     email: 'u1@aptinfo.net',
//   }
// });

// casper.thenOpen('http://phantomjs.org', function() {
//     this.echo(this.getTitle());
// });

casper.run();
