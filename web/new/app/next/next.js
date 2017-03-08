'use strict';

angular.module('myApp.next', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/next', {
    templateUrl: 'next/next.html',
    controller: 'nextCtrl'
  });
}])

.controller('nextCtrl', [function() {

}]);