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

   var userID = getCookie('userID')

  var url = window.location.href;
  var codeStart = url.search("code") + 5
  var codeEnd = url.search("state") - 1

  window.alert(url)
  window.alert(codeStart)
  window.alert(codeEnd)

  var code = url.substring(codeStart, codeEnd);
  window.alert(code)

  var error = url.search("code");

  if(error >= 0){
      if(code != 'http'){

        var url = 'http://localhost:5000/SpotifyLogin?authCode='+code +'&userID='+userID

      $.ajax({
        type:"POST",
        url: url,//'http://localhost:5000/CreateEvent',
        //data: sendData,
        async:false,
        success: function(data) {
          //console.log(data)
          //var res = $.parseJSON(data)
          //console.log(res)
          document.cookie = "spotifyLoggedIn="+1;
          //window.alert(document.chorusUser)
          //window.alert(document.chorusEvent)
          console.log(data)
          window.location.replace("/index.html#!/next")
        },
        error: function(error){
          console.log(error)
        },
        //dataType: "json"
      });

      }

    }





    function getCookie(name){
     var re = new RegExp(name + "=([^;]+)");
     var value = re.exec(document.cookie);
     return (value != null) ? unescape(value[1]) : null;
   }

   //window.alert("starting")

   var spotifyLoggedIn = getCookie('spotifyLoggedIn')
   var isHost = getCookie('isHost')


   $scope.showSettings = 0;
   $scope.showSpotify = 1;

   //window.alert("is Host: " + isHost)
   //window.alert("logged in: " + spotifyLoggedIn)
   //window.alert("show spotify: " + $scope.showSpotify)

   if(isHost == 1){
      //window.alert("if 1")
   		$scope.showSettings = 1;
   		$scope.showSpotify = 0;
   }
   else if(spotifyLoggedIn == 1){
   		//window.alert("if 2")
   		$scope.showSpotify = 0;
   }
   /*else{
      //window.alert("else")
   		$scope.showSpotify = 1;
      //window.alert($scope.showSpotify)
   }*/

//window.alert("show spotify: " + $scope.showSpotify)

}]);