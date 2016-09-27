angular.module('dbEditor', ['ngResource'])
  .factory('Table', function ($resource) {
    return $resource(':id');
  })
  .controller('tablesListController', function ($scope, Table) {
    var tablesList = this;
    tablesList.addTable = function () {
      console.log(tablesList.tableName);
      $scope.table = new Table();
      Table.save($scope.table);
    };


  });
