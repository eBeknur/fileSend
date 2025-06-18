from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from authUser.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import User

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User ro‘yxatdan o‘tdi'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"detail": "Username va password kerak."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),})
        else:
            return Response({"detail": "Login yoki parol noto‘g‘ri."},status=status.HTTP_401_UNAUTHORIZED)