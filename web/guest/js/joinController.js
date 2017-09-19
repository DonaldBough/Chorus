var myApp = angular.module("myApp", [])   
   .controller('joinCtrl', ['$scope',
  	function($scope) {
    this.greeting = 'Hello World';
}]);