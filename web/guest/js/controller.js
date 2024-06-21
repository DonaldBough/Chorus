var myApp = angular.module("myApp", [])   
   .controller('appCtrl', ['$scope',
  	function($scope) {
    this.greeting = 'Hello World';
}]);