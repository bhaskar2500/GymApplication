from django.db import models


# class Users(models.Model):
#     id=models.IntegerField(primary_key=True)
#     sellerName=models.CharField(max_length=100)
#     address=models.TextField(max_length=500)
#     phoneNumber=models.BigIntegerField(max_length=15)
#     purchasedThings=models.CharField(max_length=10)
#     purchasedQty=models.CharField(max_length=20)

#     class Meta:
#         managed=True
#         db_table='Seller'

    # def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
    #     return self.sellerName

class UsersDetails(models.Model):
    
    userName=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        managed=True
        db_table='UsersDetails'

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.userName
