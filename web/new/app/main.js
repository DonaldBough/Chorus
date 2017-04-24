'use strict';

angular.module('myApp.main', ['ngRoute'])

/*.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/index', {
    templateUrl: '/index.html',
    controller: 'mainCtrl'
  });
}])*/

.controller('mainCtrl', ["$scope", function($scope) {

    function getCookie(name){
     var re = new RegExp(name + "=([^;]+)");
     var value = re.exec(document.cookie);
     return (value != null) ? unescape(value[1]) : null;
   }

   var spotifyLoggedIn = getCookie('spotifyLoggedIn')
   var isHost = getCookie('isHost')

   $scope.showSettings = false;
   $scope.showSpotify = true;

   window.alert("logged in: " + spotifyLoggedIn)
   window.alert("show: " + $scope.showSpotify)

   if(isHost){
   		$scope.showSettings = true;
   		$scope.showSpotify = false;
   }
   else if(spotifyLoggedIn){
   		window.alert("change")
   		$scope.showSpotify = false;
   }
   else{
   		$scope.showSpotify = true;
   }

window.alert($scope.showSpotify)

}]);