import email
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from account import serializers

# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request,formate = None):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'message':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self,request,formate = None):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password = password)
            if user is not None:
                return Response({'message':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_fields_error':['Email or Password is not valid']}},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)
