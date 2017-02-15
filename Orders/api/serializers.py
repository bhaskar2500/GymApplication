from rest_framework.serializers  import  *
from django.contrib.auth import get_user_model

from Orders.Models import * 

User=get_user_model()

# class SerializeSeller(ModelSerializer):
#     class Meta:
#         model=Users

#         fields=['sellerName' 		,
#         		'id'				,
#                 'purchasedQty' 		,
#                 'address' 			,
#                 'phoneNumber' 		,
#                 'purchasedThings' ,]


class UserListSerializer(ModelSerializer):
    class Meta:
        model=User

        fields=[ 'username'		,
                 'password' 		,]
                # 'address' 			,
                # 'phoneNumber' 		,
                # 'purchasedThings' ,]

class CustomUser(ModelSerializer):
    token = CharField(read_only=True,allow_blank=True)
    username =  CharField()
   # email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',   
            'password', 
             'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
        def validate(self, data):
            print(self.data,'==============')
            username = data['username']
            password = data['password']
            user_a = User.objects.filter(username__icontains=username)
            #user_b = User.objects.filter(email__icontains=username)
            #print(username
            user_qs = (user_a).distinct()
            if user_qs.exists() and user_qs.count() == 1:
                user_obj = user_qs.first() # User.objects.get(id=1)
                password_passes = user_obj.check_password(password)
                if not user_obj.active:
                    raise ValidationError("This user is inactive")
                
                # HTTPS 
                if password_passes:
                    # token

                    payload = jwt_payload_handler(user_obj)
                    token = jwt_encode_handler(payload)
                    print(token,'-------------------')
                    data['token'] = token
                    return data
            raise ValidationError("Invalid credentials")    