from rest_framework.serializers  import *
from django.contrib.auth.models import User

from Orders.Models import * 
class SerializeSeller(ModelSerializer):
    class Meta:
        model=Users

        fields=['sellerName' 		,
        		'id'				,
                'purchasedQty' 		,
                'address' 			,
                'phoneNumber' 		,
                'purchasedThings' ,]

class CreateSellerSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username' 		,
                 'password' 	,]
                # 'address' 			,
                # 'phoneNumber' 		,
                # 'purchasedThings' ,]


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model=UsersDetails

        fields=[ 'userName' 		,
                 'password' 		,]
                # 'address' 			,
                # 'phoneNumber' 		,
                # 'purchasedThings' ,]