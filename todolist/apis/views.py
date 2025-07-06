# CRUD Operations
from django.shortcuts import get_object_or_404
from .models import Task
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import serializers , status
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def ApiOverView(request):
  api_urls = {
    'all_tasks':'/tasks',
    'add':'/task',
    'delete':'/task/pk/',
    'update':'/task/pk',
  }
  return Response(api_urls)

#Create
@api_view(['POST'])
def CreateTask(request):
  task = TaskSerializer(data = request.data)
  
  title = request.data.get('title')
  
  if Task.objects.filter(title = title).exists():
    raise serializers.ValidationError('this title already exists')
  if task.is_valid():
    task.save()
    return Response(request.data)
  else:
    return Response(status = status.HTTP_404_NOT_FOUND)

#Read
@api_view(['GET'])
def ViewTask(request):
  #checking for the params in URL
  if request.query_params:
    task = Task.objects.filter(**request.query_params.dict())
  else:
    task = Task.objects.all()  
  # Check for posts to not be empty  
  if task :
    serializer = TaskSerializer(task , many=True)
    return Response(serializer.data)
  else :
    return Response(status=status.HTTP_404_NOT_FOUND)
  

@api_view(['PUT','DELETE'])
def TaskOperation(request, pk):
  #UPDATE
  if request.method == 'PUT':
    try:
      task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  #DELETE
  elif request.method == 'DELETE':
    task = get_object_or_404(Task , pk=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  else :
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)      