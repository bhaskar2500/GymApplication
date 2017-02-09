authApp.service('api',function($resource){
          return {
            auth: $resource('/api/SellerDetails/Auth/Login/', {}, {
                login: {method: 'POST'},
                logout: {method: 'DELETE'}  
            }),
            users: $resource('/api/SellerDetails/create/', {}, {
                create: {method: 'POST'}
            })
        };
})
