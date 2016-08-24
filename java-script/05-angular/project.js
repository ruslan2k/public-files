/*global
    angular, Firebase
*/
angular.module('project', ['ngRoute', 'firebase'])

.value('fbURL', 'https://ng-projects-list.firebase.com/')
.service('fbRef', function (fbURL) {
  return new Firebase (fbURL)
})
