$(function() {

  $('body').append('<button id="log">L</logger>');
  $('body').append('<div id="logger"></div>');
  $('#logger').append('test');
  $('#log').click(function () {
    $('#logger').toggle();
  });

});
