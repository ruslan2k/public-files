// http://codepen.io/rmurphey/pen/bEzoOZ
(function () {

  function init () {
    var el = document.getElementsByTagName('button')[0];
    el.addEventListener('click', function (e) {
      var n = document.getElementsByName('number')[0].value;
      check(n);
    });
  }

  function check (value) {
    console.log('value', value);
  }

  window.onload = function () {
    init();
  };

}());
