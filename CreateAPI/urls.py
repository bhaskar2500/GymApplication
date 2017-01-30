"""
Definition of urls for CreateAPI.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Orders  import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', CreateAPI.views.home, name='home'),
    # url(r'^CreateAPI/', include('CreateAPI.CreateAPI.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^SellerDetails/$',views.details),
    url(r'^Auth/$',views.Auth),
    url(r'^api/SellerDetails/',include('Orders.api.urls',namespace='SellerDetails')),
    


]
