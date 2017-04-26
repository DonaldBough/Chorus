'use strict';

angular.module('myApp.search', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/search', {
    templateUrl: 'search/search.html',
    controller: 'searchCtrl'
  });
}])

.controller('searchCtrl', ['$scope', '$http', function($scope, $http) {
    function getCookie(name){
     var re = new RegExp(name + "=([^;]+)");
     var value = re.exec(document.cookie);
     return (value != null) ? unescape(value[1]) : null;
   }

   	var eventID = getCookie('eventID')
    var userID = getCookie('userID')

	$scope.search = function(){
		console.log($scope.searchQuery)
		var url = "https://api.spotify.com/v1/search?q=" + $scope.searchQuery + "&type=track"
		$.ajax({
   		type:"GET",
   		url: url,
   		async:false,
   		success: function(data) {
   			$scope.q = data.tracks.items
   			console.log($scope.q)
    		//$scope.q = JSON.parse(data).songs
  		},
  		error: function(error){
    		//console.log(error)
  		},
  	});
  }

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
}]);