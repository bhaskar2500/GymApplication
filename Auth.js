var authApp=angular.module('authApp', ['ngResource',"ngRoute"]).
controller('authController',authController)







//     .run(['$rootScope','$location', '$routeParams',function($rootScope,$location,$http, $routeParams) {

//    $rootScope.$on('$locationChangeSuccess', function(event, next, current,$http) {
//         $rootScope.actualLocation = $location.path();
//         // if (!(next.templateUrl ==" ")) 
//         // {  
//         //     $location.path("/index");
//         //$http.post('/Auth/');                        
//         // }
//     });        



//   }]);