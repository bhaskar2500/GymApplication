from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import *
# from Orders.Models import Users 
from rest_framework.permissions import *
#from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

from django.contrib.auth import get_user_model


class UserListAPI(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserListSerializer
    permission_classes=(AllowAny,)


class CreateSellerAPI(CreateAPIView):

    queryset=User.objects.all()
    serializer_class=CustomUser
    permission_classes=(AllowAny,)
    def create(self, request):
        
        # For Creating object in your own table
        #validated_data=request.data
        # serializer = self.get_serializer(data=request.data)
        User=get_user_model()

        user = User(
        username=request.data['username']
        )
        user.set_password(request.data['password'])
        user.save()
        return Response(request.data)

     

        # From the django's buildin 
        #print(request.data["password"])
        #user=User.objects.create_user(username=request.data['userName'],password=request.data['password'])
        #return HttpResponse('Registerd Succesfully')

class UpdateSellerAPI(UpdateAPIView):

    queryset=User.objects.all()
    serializer_class=UserListSerializer
    lookup_field='sellerName'


class AuthView(CreateAPIView):
    #authentication_classes = (QuietBasicAuthentication,)
    queryset=User.objects.all()
    serializer_class=CustomUser
    permission_classes=(AllowAny,)

        
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CustomUser(data=data)
        #print(serializer)
        if serializer.is_valid(raise_exception=True):

            new_data = serializer.data
            print(new_data,',,,')
            
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        # username=request.data['username']         
        # password=request.data['password']
        # user=authenticate(username=username,password=password)
        # print(user.username) 
        # if user is not None and user.username != 'admin':
        #     print('logged in')
        #     login(request, user)        
        #     return Response(request.data)
        # return Response({}) 
    def delete(self, request, *args, **kwargs):
        logout(request) 
        return Response({'logout':'yes'})