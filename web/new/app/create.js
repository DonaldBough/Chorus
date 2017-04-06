'use strict';
angular.module('myApp.create', []).
controller('createCtrl', ['$scope', '$http', function ($scope, $http) {
	$scope.check = true;
	var url = window.location.href;
	//window.alert(url);

	var codeStart = url.search("code") + 5
	var codeEnd = url.search("state") - 1
	var code;
	code = url.substring(codeStart, codeEnd);

	var error = url.search("error");

	$scope.createEvent = function(){
		
		window.location.replace("https://accounts.spotify.com/en/authorize?client_id=0abc049d139f4ee8b465fd9416aa358d&response_type=code&redirect_uri=http:%2F%2Flocalhost:8000%2Fcreate.html&scope=user-read-private%20user-read-email%20playlist-read-private%20playlist-read-collaborative%20playlist-modify-public%20playlist-modify-private&state=34fFs29kd09")
		
		if(error >= 0){
			window.alert("an error occured")
		}
		else{
			if(code != 'http'){

				var data = {
					"password": $scope.eventCode,
					"explicit": $scope.check,
					"authCode":  code
				}
				data = JSON.stringify(data);

			}

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

		}

	}
}]);