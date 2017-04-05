'use strict';

angular.module('myApp.create', [])

.controller('createCtrl', function($scope) {
	self = this;
	$scope.test = "123";

	function test(){
		window.alert("test function")
	}

});