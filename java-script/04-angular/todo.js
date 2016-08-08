angular.module('todoApp', [])
  .controller('todoListCtrl', TodoListCtrl);

function TodoListCtrl ($scope) {
  $scope.todos = [
    {text: 'bla'},
    {text: 'abc'},
  ];
}



angular.module("diveLog", [])
  .controller('diveLogCtrl', DiveLogCtrl);


function DiveLogCtrl ($scope) {
  $scope.totalDives = 4;
  $scope.dives = [
    {text: "text 1"},
    {text: "text 2"},
    {text: "text 3"},
  ];
}
