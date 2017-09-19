'use strict';

angular.module('myApp.settings', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/settings', {
    templateUrl: 'settings/settings.html',
    controller: 'settingsCtrl'
  });
}])

.controller('settingsCtrl', [function() {

}]);