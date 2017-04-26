	'use strict';

  angular.module('myApp.next', ['ngRoute'])

  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/next', {
      templateUrl: 'next/next.html',
      controller: 'nextCtrl'
    });
  }])

  .controller('nextCtrl', ['$scope', '$http', '$interval', function ($scope, $http, $interval) {
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
  var url2 = 'http://localhost:5000/GetQueue?userid='+ userID +'&eventid='+ eventID

  var getNext = function(){

  $.ajax({
   type:"POST",
   url: url2,
   async:false,
   success: function(data) {
    $scope.q = JSON.parse(data).songs
  },
  error: function(error){
    console.log(error)
  },
  });

  }


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
    getNext()
    },5000);


}]);