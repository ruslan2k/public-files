angular.module('todoApp', [])
  .controller('todoListCtrl', TodoListCtrl)
  .factory('todoAppApi', todoAppApi)
  .constant('apiUrl', '/api');

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
    todoAppApi.getTodos()
      .success(function (data) {
        // --- Resolved handler
        console.log('OK data', data);
        $scope.todos = data;
        loading = false;
      })
      .error(function (reason) {
        console.log('error');
        $scope.errorMessage = reason;
        loading = false;
      });
  }
}

function todoAppApi ($http, apiUrl) {
  //var todos = [
  //  {text: "abc"},
  //  {text: "def"},
  //  {text: "ghi"},
  //];
  //var counter = 0;

  return {
    getTodos: function () {
      var url = apiUrl + '/todos';
      return $http.get(url);
    }
    // getTodos: function () {
    //   var deferred = $q.defer();
    //   counter++;
    //   setTimeout(function () {
    //     if (counter % 3 == 0) {
    //       deferred.reject('Error: Call counter is ' + counter);
    //     } else {
    //       deferred.resolve(todos);
    //     }
    //   }, 2000);
    //   return deferred.promise;
    // }
  };
}
