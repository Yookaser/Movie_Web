from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse, HttpResponse
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_user_data(request):
    token = request.headers['Authorization'][7:]
    access_token = AccessToken(token)
    
    data = {
                'user_id': access_token['user_id'],
            }
    return JsonResponse(data)
