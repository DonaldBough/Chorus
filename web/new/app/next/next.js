	'use strict';

angular.module('myApp.next', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/next', {
    templateUrl: 'next/next.html',
    controller: 'nextCtrl'
  });
}])

.controller('nextCtrl', [function() {
		function getCookie(name){
    		var re = new RegExp(name + "=([^;]+)");
    		var value = re.exec(document.cookie);
    		return (value != null) ? unescape(value[1]) : null;
  		}

  		var eventID = getCookie('eventID')
  		var hostID = getCookie('userID')
  		var isHost = getCookie('isHost')
		
		window.alert(eventID + " " + hostID + " " + isHost)

    var url = 'http://localhost:5000/GetQueue?userID='+ userID +'&eventID='+ eventID


    $.ajax({
        type:"POST",
        url: url,//'http://localhost:5000/CreateEvent',
        //data: sendData,
        async:false,
        success: function(data) {
          console.log(data)
          window.location.replace("/index.html#!/next")
        },
        error: function(error){
          console.log(error)
        },
        //dataType: "json"
      });


		/*
		document.chorusUser
		document.chorusEvent = res.eventID;
		document.chorusIsHost = true;*/
		//window.alert(document.cookie)
}]);