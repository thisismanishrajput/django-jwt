import email
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from account import serializers
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,formate = None):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'message':'Registration Successful','data':token},
                status=status.HTTP_201_CREATED,
               
                )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self,request,formate = None):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password = password)
            token = get_tokens_for_user(user)
            if user is not None:
                return Response({
                    'status':status.HTTP_200_OK,
                    'message':'Login Success',
                    'data':token
                    }
                    ,status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_fields_error':['Email or Password is not valid']}},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format= None):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response({
                'message':'Given Profile Successfully',
                'data':serializer.data},
                status=status.HTTP_201_CREATED,
               
                )


class UserChangePassword(APIView):
    pass