from django.conf.urls import include, url
from   .views import *
                      

urlpatterns=[

    url(r'^details/$',UserListAPI.as_view(),name="list"),
    url(r'^create/$',CreateSellerAPI.as_view(),name="create"),
     url(r'(?P<sellerName>[\d]+)/edit/$',UpdateSellerAPI.as_view(),name="create"),
     url(r'^Auth/Login/$',AuthView.as_view(),name="auth")
       
    ]
