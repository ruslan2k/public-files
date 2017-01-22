$(function() {

  function init (element) {
    $(element).append('<div><button id="log">log</button></div>');
    $('<div/>', {
      id: 'logger',
      css: {
        border: '1px solid',
        display: 'none',
      }
    }).appendTo(element);

    $('#log').click(function () {
      $('#logger').toggle();
    });

    console.olog = console.log;
    console.log = function (message) {
      console.olog(message);
      $('#logger').append(message + '<br/>');
    }
  }

  init('#logging');

  $('#test').click(function () {
    console.log('test');
    // $.ajax({
    //   url: "https://wm.exchanger.ru/asp/XMLWMList.asp?exchtype=17",
    // }).done(function () {
    //   console.log('ajax - ok');
    // });
  });
 
  function timeout () {
    setTimeout( function () {
      console.log('tick');
      timeout();
    }, 10000);
  }

  timeout();

});
