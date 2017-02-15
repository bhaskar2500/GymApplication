authApp.config(['$httpProvider','$resourceProvider', '$routeProvider', function($httpProvider,$resourceProvider,$routeProvider){
        // django and angular both support csrf tokens. This tells
        // angular which cookie to add to what header.
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider.when("/index",{templateUrl:"/SellerDetails",controller:"authController"});
        

    }])

    