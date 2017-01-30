from django.contrib import admin
from django.db import models
from  .Models import UsersDetails


class OrdersAdmin(admin.ModelAdmin):
    class Meta:
        model=UsersDetails
    class Media:

        js=("https://code.jquery.com/jquery-3.1.1.min.js",'js/newfile.js',)


        
admin.site.register(UsersDetails,OrdersAdmin)


    






