'use strict';

angular.module('myApp.join', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/join', {
    templateUrl: 'join/join.html',
    controller: 'joinCtrl'
  });
}])

.controller('joinCtrl', [function() {

}]);