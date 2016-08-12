angular.module('todoApp', [])
  .controller('todoListCtrl', TodoListCtrl)
  .factory('todoAppApi', todoAppApi);

function TodoListCtrl ($scope, todoAppApi) {
  $scope.todos = [];
  $scope.errorMessage = '';
  $scope.isLoading = isLoading;
  $scope.refreshTodos = refreshTodos;

  var loading = false;

  function isLoading () {
    return loading;
  }

  function refreshTodos () {
    loading = true;
    $scope.todos = [];
    $scope.errorMessage = '';
    todoAppApi.getTodos().then(
      function (data) {
        // --- Resolved handler
        console.log('resolved' + data);
        $scope.todos = data;
        loading = false;
        //$scope.$apply();
      },
      function (reason) {
        console.log('error');
        $scope.errorMessage = reason;
        loading = false;
      });
  }
}

function todoAppApi ($q) {
  var todos = [
    {text: "abc"},
    {text: "def"},
    {text: "ghi"},
  ];
  var counter = 0;

  return {
    getTodos: function () {
      var deferred = $q.defer();
      counter++;
      setTimeout(function () {
        if (counter % 3 == 0) {
          deferred.reject('Error: Call counter is ' + counter);
        } else {
          deferred.resolve(todos);
        }
      }, 2000);
      return deferred.promise;
    }
  };
}
