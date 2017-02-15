var authController=function($scope, api,$window,$location) {
    $scope.getCredentials = function(){
            return {username: $scope.username, password: $scope.password};
        };

          function changeUser(user) {
            angular.extend(currentUser, user);
        }
        
        $scope.login = function(){
            api.auth.login($scope.getCredentials()).    
                $promise.then(function(data)
                {
                    console.log(data);
                    $window.localStorage['jwtToken']=data.token;
                    var saveToken =$window.localStorage['jwtToken'] ;
                    var isAuthed = function() {
                    var token = self.getToken();
                     if(saveToken) {
                        var params = self.parseJwt(saveToken);
                         return true;
                        } 
                    else {
                        return false;
                        }
                    }
                    if(isAuthed())                   
                        {
                        $scope.user = data.username;
                        alert();    
                        }

                    
                    if(data.username ==null){
                        alert('Incorrect username/password');
                    }
                    else{
                        $location.url('/index');
                    }
                
                }).catch(function(data){
                        // on incorrect username and password
              
                        alert('incorrect data');
                       

                    });
        };
 
        $scope.logout = function(){
            api.auth.logout(function(){
                $scope.user = undefined;
                self.logout = function() {
                $window.localStorage.removeItem('jwtToken');
            }
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
}