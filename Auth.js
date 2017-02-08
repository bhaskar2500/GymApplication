var authApp=angular.module('authApp', ['ngResource',"ngRoute"]).
    controller('authController', function($scope, api,$location) {
        // $('#id_auth_form input').checkAndTriggerAutoFillEvent();
 
        $scope.getCredentials = function(){
            return {username: $scope.username, password: $scope.password};
        };
        $scope.login = function(){
            api.auth.login($scope.getCredentials()).
                $promise.then(function(data)
                {
                    $scope.user = data.username;
                    if(data.username ==null){
                        alert('Incorrect username/password');
                    }
                    else{
                        $location.url('/index');
                    }
                    
                }).catch(function(data){
                        // on incorrect username and password
                        alert('incorrect data')
                    });
        };
 
        $scope.logout = function(){
            api.auth.logout(function(){
                $scope.user = undefined;
            });
        };
        $scope.register = function($event){
            // prevent login form from firing
            $event.preventDefault();
            // create user and immediatly login on success
            api.users.create($scope.getCredentials()).
                $promise.then($scope.login).
                    catch(function(data){
                        alert(data.data.username);
                    });
            };
    });









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