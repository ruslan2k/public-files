angular.module('dbEditor', [])
  .controller('tablesListController', function () {
    var tablesList = this;
    tablesList.addTable = function () {
      console.log(tablesList.tableName);
    };


  });
