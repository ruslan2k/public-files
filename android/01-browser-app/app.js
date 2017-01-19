$(function() {

  $('body').append('<button id="log">L</logger>');
  $('body').append('<div id="logger"></div>');
  $('#logger').append('test');
  $('#log').click(function () {
    $('#logger').toggle();
  });

  console.olog = console.log;
  console.log = function (message) {
    console.olog(message);
    $('#logger').append('<p>' + message + '</p');
  }

  $('#test').click(function () {
    console.log('test');
  });

});
