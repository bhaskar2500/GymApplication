var authApp=angular.module('authApp', ['ngResource',"ngRoute"]).
    config(['$httpProvider','$resourceProvider', '$routeProvider', function($httpProvider,$resourceProvider,$routeProvider){
        // django and angular both support csrf tokens. This tells
        // angular which cookie to add to what header.
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider.when("/index",{templateUrl:"/SellerDetails",controller:"authController"});
        

    }]).
    service('api', function($resource){
          return {
            auth: $resource('/api/SellerDetails/Auth/Login/', {}, {
                login: {method: 'POST'},
                logout: {method: 'DELETE'}  
            }),
            users: $resource('/api/SellerDetails/create/', {}, {
                create: {method: 'POST'}
            })
        };
    }).
    controller('authController', function($scope, api,$location) {
        // $('#id_auth_form input').checkAndTriggerAutoFillEvent();
 
        $scope.getCredentials = function(){
            return {username: $scope.username, password: $scope.password};
        };
       
 
        $scope.login = function(){
            api.auth.login($scope.getCredentials()).
                $promise.
                    then(function(data){
                    $scope.user = data.username;
                    if(data.username ==null)
                    {
                        alert('incorrect data');
                    }
                    else{
                        $location.url('/index');
                    }
                    
                    }).
                    catch(function(data)
                    {
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
                $promise.
                    then($scope.login).
                    catch(function(data){
                        alert(data.data.username);
                    });
            };
    }).run(['$rootScope','$location', '$routeParams',function($rootScope,$location,$http, $routeParams) {

   $rootScope.$on('$locationChangeSuccess', function(event, next, current,$http) {
        $rootScope.actualLocation = $location.path();
        // if (!(next.templateUrl ==" ")) 
        // {  
        //     $location.path("/index");
        $http.post('/Auth/');                        
        // }
    });        



  }]);