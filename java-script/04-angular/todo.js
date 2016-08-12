angular.module('todoApp', [])
  .controller('todoListCtrl', TodoListCtrl)
  .factory('todoAppApi', todoAppApi);

function TodoListCtrl ($scope, todoAppApi) {
  $scope.todos = todoAppApi.getTodos();
  //$scope.todos = [];
  //$scope.isLoading = isloading;
  //$scope.refreshTodos = refreshTodos;

  //var loading = false;

  //function isloading () {
  //  return loading;
  //}

  //function refreshTodos () {
  //  loading = true;
  //  $scope.todos = [];
  //  setTimeout( function () {
  //    $scope.todos = todoAppApi.getTodos();
  //    loading = false;
  //    $scope.$apply();
  //  }, 2000);
  //}
}

function todoAppApi () {
  var todos = [
    {text: "abc"},
    {text: "def"},
    {text: "ghi"},
  ];

  return {
    getTodos: function () {
      return todos;
    }
  };
}
