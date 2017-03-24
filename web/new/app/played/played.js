'use strict';

angular.module('myApp.played', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/played', {
    templateUrl: 'played/played.html',
    controller: 'playedCtrl'
  });
}])

.controller('playedCtrl', [function() {

}]);