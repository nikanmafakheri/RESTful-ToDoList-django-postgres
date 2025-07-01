# CRUD Operations
from django.shortcuts import render
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import serializers , status

@api_view(['GET'])
def ApiOverView(request):
  api_urls = {
    'all_posts':'/',
    'add':'/create',
    'delete':'post/pk/delete',
    'update':'/update/pk',
  }
  return Response(api_urls)

#Create
@api_view(['POST'])
def CreatePost(request):
  post = PostSerializer(data = request.data)
  
  title = request.data.get('title')
  
  if Post.objects.filter(title = title).exists():
    raise serializers.ValidationError('this title already exists')
  if post.is_valid():
    post.save()
    return Response(request.data)
  else:
    return Response(status = status.HTTP_404_NOT_FOUND)

#Read
@api_view(['GET'])
def ViewPost(request):
  #checking for the params in URL
  if request.query_params:
    post = Post.objects.filter(**request.query_params.dict())
  else:
    post = Post.objects.all()  
  # Check for posts to not be empty  
  if post :
    serializer = PostSerializer(post , many=True)
    return Response(serializer.data)
  else :
    return Response(status=status.HTTP_404_NOT_FOUND)