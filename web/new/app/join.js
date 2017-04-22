'use strict';
angular.module('myApp.join', []).
controller('joinCtrl', ['$scope', '$http', function ($scope, $http) {
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

				$.ajax({
					type:"POST",
				url: url,
				async:false,
				success: function(data) {
					//console.log(data)
					var res = $.parseJSON(data)
					//console.log(res)
					document.cookie = "eventID="+res.eventID;
					document.cookie = "eventName="+$scope.eventCode;
					document.cookie = "userID="+res.hostID;
					document.cookie = "isHost="+false;
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