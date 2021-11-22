from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from movies.models import Movie, Actor
from django.contrib.auth import get_user_model
from .models import MovieReview, ActorReview, MovieComment, ActorComment
from .serializers import (
    MovieReviewListSerializer, 
    MovieReviewSerializer, 
    ActorReviewListSerializer, 
    ActorReviewSerializer, 
    MovieCommentSerializer, 
    ActorCommentSerializer,
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_review_read_all(request):
    reviews = MovieReview.objects.all()
    serializer = MovieReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_review_read(request, movie_pk):
    reviews = MovieReview.objects.filter(movie=movie_pk)
    serializer = MovieReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def movie_review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def movie_review_read_update_delete(request, review_pk):
    review = get_object_or_404(MovieReview, pk=review_pk)
    if request.method == 'GET':
        serializer = MovieReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT': 
        serializer = MovieReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def actor_review_read_all(request):
    reviews = ActorReview.objects.all()
    serializer = ActorReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def actor_review_read(request, actor_pk):
    reviews = ActorReview.objects.filter(actor=actor_pk)
    serializer = ActorReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def actor_review_create(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, actor=actor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def actor_review_read_update_delete(request, review_pk):
    review = get_object_or_404(ActorReview, pk=review_pk)
    if request.method == 'GET':
        serializer = ActorReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def movie_create_comment(request, review_pk):
    review = get_object_or_404(MovieReview, pk=review_pk)
    serializer = MovieCommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True): 
        serializer.save(user=request.user, review=review)   
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def actor_create_comment(request, review_pk):
    review = get_object_or_404(ActorReview, pk=review_pk)
    serializer = ActorCommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True): 
        serializer.save(user=request.user, review=review)   
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def movie_comment_update_delete(request, comment_pk):
    comment = get_object_or_404(MovieComment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = MovieCommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
def actor_comment_update_delete(request, comment_pk):
    comment = get_object_or_404(ActorComment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = ActorCommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk },  status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like_dislike(request, category, review_pk, flag):
    if request.user.is_authenticated:
        if category == 'movie': review = get_object_or_404(MovieReview, pk=review_pk)
        else: review = get_object_or_404(ActorReview, pk=review_pk)
        
        if flag:
            if review.like_users.filter(pk=request.user.pk).exists():
                review.like_users.remove(request.user)
                liked = False
            else:
                review.like_users.add(request.user)
                liked = True
            like_status = {
                'liked': liked,
            }
        else:
            if review.dislike_users.filter(pk=request.user.pk).exists():
                review.dislike_users.remove(request.user)
                disliked = False
            else:
                review.dislike_users.add(request.user)
                disliked = True
            like_status = {
                'disliked': disliked,
            }
        return JsonResponse(like_status)
    return HttpResponse(status=401)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_movie_review(request, user_pk):
    reviews = MovieReview.objects.filter(user=user_pk)
    serializer = MovieReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_actor_review(request, user_pk):
    reviews = ActorReview.objects.filter(actor=user_pk)
    serializer = ActorReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
