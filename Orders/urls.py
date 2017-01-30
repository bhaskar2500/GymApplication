from django.conf.urls import include, url
from . import views
urlpatterns=[
    
        url(r'^$', include(views.details)),
    
         url(r'^create/$',include(views.CreateSellerAPI),namespace='SellerDetails')),
    ]