var myApp = angular.module("myApp", [])   
   .controller('createCtrl', ['$scope',	'$http',
  	function($scope, $http) {
  		self = this;
  		self.check = false;
  		var eventID
    $scope.create = function(){
    	var params = "{password:" + eventCode + ", explicit:" + self.check + "}"
    	//window.alert("test:" + self.eventCode);
    	$http

      .post(url: 'localhost/CreateEvent', params)
    	.success(function(data, status, headers, config) {
    		window.location('/index.html');
    		eventID = data.EventId; 
        console.log(data);
      }).
      error(function(data, status, headers, config) {
      	window.alert("An error occured");
      });
    }

}]);