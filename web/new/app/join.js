'use strict';
angular.module('myApp.join', []).
controller('joinCtrl', ['$scope', '$http', function ($scope, $http) {
	
	function getCookie(name){
    		var re = new RegExp(name + "=([^;]+)");
    		var value = re.exec(document.cookie);
    		return (value != null) ? unescape(value[1]) : null;
  		}


	$scope.check = true;
	var url = window.location.href;

	var codeStart = url.search("code") + 5
	var codeEnd = url.search("state") - 1
	var code;
	code = url.substring(codeStart, codeEnd);

	var error = url.search("error");

	$scope.joinEvent = function(){
				console.log($scope.eventCode)

				var url = 'http://localhost:5000/JoinEvent?password='+$scope.eventCode
				console.log(url)

				$.ajax({
					type:"POST",
				url: url,
				async:false,
				success: function(data) {
					//console.log(data)
					var res = 	JSON.parse(data)
					//window.alert(res.EventID)
					document.cookie = "eventID="+ res.eventID;
					document.cookie = "eventName="+ $scope.eventCode;
					//window.alert(res.userID)
					document.cookie = "userID="+ res.userID;
					document.cookie = "isHost="+ 0;
					document.cookie = "spotifyLoggedIn="+ 0;

					console.log(getCookie('eventID'))

					//window.alert(document.chorusUser)
					//window.alert(document.chorusEvent)
					console.log(data)
					window.location.replace("/index.html#!/next")
				},
				error: function(error){
					console.log(error)
					window.alert("an error occured")
				},
				//dataType: "json"
			});
		}
	}]);