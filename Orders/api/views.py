from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import *
from Orders.Models import Users 
from .authentication import QuietBasicAuthentication
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.models import User

class SellerListAPI(ListAPIView):
    queryset=Users.objects.all()
    serializer_class=SerializeSeller


class CreateSellerAPI(CreateAPIView):

    queryset=User.objects.all()
    serializer_class=CreateSellerSerializer
    def create(self, request):
        
        # For Creating object in your own table
        #validated_data=request.data
        # serializer = self.get_serializer(data=request.data)
        
        #validated_data['password'] = make_password(validated_data['password']
        # serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        # print(serializer)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, headers=headers)


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

    queryset=Users.objects.all()
    serializer_class=CreateSellerSerializer
    lookup_field='sellerName'


class AuthView(CreateAPIView):
    #authentication_classes = (QuietBasicAuthentication,)
    serializer_class=CreateUserSerializer

 
    def post(self, request, *args, **kwargs):

      
        username=request.data['username']         
        password=request.data['password']
        user=authenticate(username=username,password=password)
        print(user.username)
        if user is not None and user.username != 'admin':
            print('logged in')
            login(request, user)        
            return Response(request.data)
        return Response({}) 
    def delete(self, request, *args, **kwargs):
        logout(request) 
        return Response({'logout':'yes'})