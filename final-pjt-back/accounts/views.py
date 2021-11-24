from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse, HttpResponse
from .models import Userinfo, UserMovie
from movies.models import Movie
from .serializers import UserSerializer, UserAdditionalSerializer, UserMovieserializer


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


@api_view(['GET', 'POST', 'PUT'])
def user_additional(request):
    try:
        user = get_object_or_404(Userinfo, user=request.user)
    except:
        post = True
    if request.method == 'GET':
        serializer = UserAdditionalSerializer(user)
        return Response(serializer.data)
    elif request.method == 'POST':
        if post:
            serializer = UserAdditionalSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True): 
                serializer.save(user=request.user)   
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        serializer = UserAdditionalSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_movies(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            movies = UserMovie.objects.filter(user=request.user)
            serializer = UserMovieserializer(movies, many=True)
            return Response(serializer.data)
        else:
            movie_pk = request.data['movie_pk']
            movie = Movie.objects.get(pk=movie_pk)
            if UserMovie.objects.filter(user=request.user).filter(movie=movie).exists():
                UserMovie.objects.filter(user=request.user).filter(movie=movie).delete()
                liked = False
            else:
                UserMovie.objects.create(user=request.user, movie=movie)
                liked = True
            status = {
                'liked': liked,
            }
        return JsonResponse(status)
    return HttpResponse(status=401)
