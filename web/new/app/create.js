'use strict';
angular.module('myApp.create', []).
controller('createCtrl', ['$scope', '$http', function ($scope, $http) {

	var url = window.location.href;
	//window.alert(url);

	var codeStart = url.search("code") + 5
	var codeEnd = url.search("state") - 1
	var code;

	var error = url.search("error");

	if(error >= 0){
		//window.alert("an error occured")
	}
	else{
		code = url.substring(codeStart, codeEnd);
		window.alert(code)
		
		var data = {
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri":  "http:%2F%2Flocalhost:8000%2Fcreate.html"
		}
		data = JSON.stringify(data);

		}
		$http.post('https://accounts.spotify.com/api/token',data)
		.then(function successCallback(response) {
    		// this callback will be called asynchronously
    		// when the response is available
    		//window.alert(data)
  		}, function errorCallback(response) {
    		// called asynchronously if an error occurs
    		// or server returns response with an error status.
    		//window.alert("error" + status)
  		});

	$scope.createEvent = function(){
		window.location.replace("https://accounts.spotify.com/en/authorize?client_id=0abc049d139f4ee8b465fd9416aa358d&response_type=code&redirect_uri=http:%2F%2Flocalhost:8000%2Fcreate.html&scope=user-read-private%20user-read-email%20playlist-read-private%20playlist-read-collaborative%20playlist-modify-public%20playlist-modify-private&state=34fFs29kd09")
		
	}
}]);