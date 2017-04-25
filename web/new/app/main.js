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

   window.alert("starting")

   var spotifyLoggedIn = getCookie('spotifyLoggedIn')
   var isHost = getCookie('isHost')


   $scope.showSettings = 0;
   $scope.showSpotify = 1;

   window.alert("is Host: " + isHost)
   window.alert("logged in: " + spotifyLoggedIn)
   window.alert("show spotify: " + $scope.showSpotify)

   if(isHost == 1){
      window.alert("if 1")
   		$scope.showSettings = 1;
   		$scope.showSpotify = 0;
   }
   else if(spotifyLoggedIn == 1){
   		window.alert("if 2")
   		$scope.showSpotify = 0;
   }
   /*else{
      window.alert("else")
   		$scope.showSpotify = 1;
      window.alert($scope.showSpotify)
   }*/

window.alert("show spotify: " + $scope.showSpotify)

}]);