'use strict';

angular.module('myApp.suggest', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/suggest', {
    templateUrl: 'suggest/suggest.html',
    controller: 'suggestCtrl'
  });
}])

.controller('suggestCtrl', [function() {

}]);