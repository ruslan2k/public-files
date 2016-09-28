angular.module('dbEditor', ['ngResource'])
  .factory('Table', function ($resource) {
    return $resource(':id');
  })
  .controller('tablesListController', function ($scope, Table) {
    var tablesList = this;
    tablesList.addTable = function () {
      console.log(tablesList.tableName);
      $scope.table = new Table();
      $scope.table.name = tablesList.tableName;
      Table.save($scope.table);
    };


  });
