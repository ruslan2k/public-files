(function () {

  function init () {
    var el = document.getElementsByTagName('button')[0];
    el.addEventListener('click', function () {
      console.log('ok');
    });
  }

  function check (value) {
  }

  init();
  console.log('ok');

}());
