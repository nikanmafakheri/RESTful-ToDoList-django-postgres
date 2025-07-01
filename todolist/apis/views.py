from django.shortcuts import render
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def ApiOverView(request):
  api_urls = {
    'all_posts':'/',
    'add':'/create',
    'delete':'post/pk/delete',
    'update':'/update/pk',
  }
  return Response(api_urls)