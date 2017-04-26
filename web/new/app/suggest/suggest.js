	'use strict';

  angular.module('myApp.suggest', ['ngRoute'])

  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/suggest', {
      templateUrl: 'suggest/suggest.html',
      controller: 'suggestCtrl'
    });
  }])

  .controller('suggestCtrl', ['$scope', '$http', '$interval', function ($scope, $http, $interval) {
    $scope.q

    var eventID = getCookie('eventID')
    var userID = getCookie('userID')
    var isHost = getCookie('isHost')

    function getCookie(name){
     var re = new RegExp(name + "=([^;]+)");
     var value = re.exec(document.cookie);
     return (value != null) ? unescape(value[1]) : null;
   }

   $scope.sendVote = function(songID){
    window.alert("vote1")
    var url = 'http://localhost:5000/SendVote?userID='+
    userID +'&eventID='+ eventID + "&songID=" +
    songID + "&vote="+ 1 + "&veto=" + 0

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

  $scope.sendVeto = function(songID){
    window.alert("vote1")
    var url = 'http://localhost:5000/SendVote?userID='+
    userID +'&eventID='+ eventID + "&songID=" +
    songID + "&vote="+ 0 + "&veto=" + 1

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

  var url = 'http://localhost:5000/GetQueue?userid='+ userID +'&eventid='+ eventID

  var getData = function(){

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

  }

  getData()

  $interval(function(){
    getData()
    },10000);


}]);