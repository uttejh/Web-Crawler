var app = angular.module("crawler",['ui.router']);

app.config(function($stateProvider,$urlRouterProvider){
	$urlRouterProvider.otherwise("/home");

	$stateProvider.
		state('home',{
			url:'/home',
			views:{
				"main":{
					templateUrl:"partials/home.html",
					data:{title:"Home"},
					controller:"HomeController"
				}
			}
		});
});