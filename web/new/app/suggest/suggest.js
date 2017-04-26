'use strict';

angular.module('myApp.suggest', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/suggest', {
    templateUrl: 'suggest/suggest.html',
    controller: 'suggestCtrl'
  });
}])

.controller('suggestCtrl', ['$scope', '$http', function($scope, $http) {
    function getCookie(name){
     var re = new RegExp(name + "=([^;]+)");
     var value = re.exec(document.cookie);
     return (value != null) ? unescape(value[1]) : null;
   }

   	var eventID = getCookie('eventID')
    var userID = getCookie('userID')


   $scope.sendVote = function(songID, song, artist){
    window.alert("vote1")
    var url = 'http://localhost:5000/AddToQueue?eventID='+ eventID + "&songID=" + songID + "&songName="+ song + "&artist=" + artist

    $.ajax({
     type:"POST",
     url: url,
     async:false,
     success: function(data) {
     },
     error: function(error){
      console.log(error)
    },
  });
    window.alert("vote2")
  }

var getData = function(){
  var url2 = 'http://localhost:5000/GetSuggestedSongs?eventID='+ eventID

  $.ajax({
   type:"POST",
   url: url2,
   async:false,
   success: function(data) {
    console.log(data)
    $scope.s = data.tracks//JSON.parse(JSON.stringify(data)).tracks
  },
  error: function(error){
    console.log(error)
  },
  });

  }

getData()

}]);