angular.module('editor', [])
  .controller('itemCtrl', function ($scope) {
    //var itemList = this;
    $scope.items = [
      {value: "one"},
      {value: "two"},
      {value: "three"},
    ];
  });
