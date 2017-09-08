var app = angular.module("crawler",['ui.router','rzModule','ngAnimate','ui.bootstrap']);

app.config(function($stateProvider,$urlRouterProvider){
	$urlRouterProvider.otherwise("/home");

	$stateProvider
		.state('home',{
			url:'/home',
			views:{
				"main":{
					templateUrl:"partials/home.html",
					data:{title:"Home"},
					controller:"HomeController"
				}
			}
		})
		.state('MobileFinder',{
			url:'/MobileFinder',
			views:{
				"main":{
					templateUrl:"partials/mobile_finder.html",
					data:{title:"Mobile Finder"},
					controller:"MobileFinderController"
				}
			}
		})
		.state('Compare',{
			url:'/Compare',
			views:{
				"main":{
					templateUrl:"partials/compare.html",
					data:{title:"Compare"},
					controller:"CarouselController"
				},
				"content@Compare":{
					templateUrl:"partials/carousel.html",
					controller:"CarouselController"
				}
			}
		});
});