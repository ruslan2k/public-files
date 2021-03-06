/*global
    angular, Firebase
*/
angular.module('project', ['ngRoute', 'firebase'])

.value('fbURL', 'https://ng-projects-list.firebase.com/')
.service('fbRef', function (fbURL) {
  return new Firebase (fbURL);
})
.service('fbAuth', function ($q, $firebase, $firebaseAuth, fbRef) {
  var auth;
  return function () {
    if (auth) {
      return $q.when(auth);
    }
    var authObj = $firebaseAuth(fbRef);
    if (authObj.$getAuth()) {
      return $q.when(auth = authObj.$getAuth());
    }
    var deferred = $q.defer();
    authObj.$authAnonymously().then(function (authData) {
      auth = authData;
      deferred.resolve(authData);
    });
    return deferred.promise;
  };
})

.service('Projects', function ($q, $firebase, fbRef, fbAuth, projectListValue) {
  // FIXME
})

;