'use strict';
angular.module('myApp.create', []).
controller('createCtrl', ['$scope', '$http', function ($scope, $http) {
	$scope.check = true;
	var url = window.location.href;

	var codeStart = url.search("code") + 5
	var codeEnd = url.search("state") - 1
	var code;
	code = url.substring(codeStart, codeEnd);

	var error = url.search("error");

	$scope.createEvent = function(){

		/*var successAlert = function(response){
			window.alert("success123")
			console.log(response)
		}*/
		window.location.replace("https://accounts.spotify.com/en/authorize?client_id=0abc049d139f4ee8b465fd9416aa358d&response_type=code&redirect_uri=http:%2F%2Flocalhost:8000%2Fcreate.html&scope=user-read-private%20user-read-email%20playlist-read-private%20playlist-read-collaborative%20playlist-modify-public%20playlist-modify-private&state=34fFs29kd09")
		
		if(error >= 0){
			window.alert("an error occured")
		}
		else{
			if(code != 'http'){

				var data = {
					"eventName": $scope.eventCode,
					"explicitAllowed": 1,//$scope.check,
					"authCode":  code
				}
				data = JSON.stringify(data);

			$.ajax({
				type:"POST",
				url: 'http://localhost:5000/CreateEvent',
				data: sendData,
				success: function(data) {
					console.log(data)
				},
				error: function(error){
					console.log(error)
				},
				dataType: "json"
			});

			}

		}
	}
			/*
			$http.post('http://localhost:5000/CreateEvent',data)
			.then(function successCallback(response) {
				window.location.replace('http://localhost:8000/index.html#!/next')
    			// this callback will be called asynchronously
    			// when the response is available
    			//window.alert(data)
    		}, function errorCallback(response) {
    			window.alert(error)
    			// called asynchronously if an error occurs
    			// or server returns response with an error status.
    			//window.alert("error" + status)
    		});
			*/

}]);