	'use strict';

  angular.module('myApp.played', ['ngRoute'])

  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/played', {
      templateUrl: 'played/played.html',
      controller: 'playedCtrl'
    });
  }])

  .controller('playedCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.q

    var eventID = getCookie('eventID')
    var userID = getCookie('userID')
    var isHost = getCookie('isHost')

    function getCookie(name){
     var re = new RegExp(name + "=([^;]+)");
     var value = re.exec(document.cookie);
     return (value != null) ? unescape(value[1]) : null;
   }

  var url = 'http://localhost:5000/GetPlayedSongs?userid='+ userID +'&eventid='+ eventID

  $.ajax({
   type:"POST",
   url: url,
   async:false,
   success: function(data) {
    $scope.q = JSON.parse(data).songs
  },
  error: function(error){
    console.log(error)
  },
});
}]);