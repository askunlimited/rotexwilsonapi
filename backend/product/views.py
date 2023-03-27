from django.shortcuts import render
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ViewSet):
  queryset = Category.objects.all()
  
  def list(self, request):
    serializer = CategorySerializer(self.queryset, many=True)
    return Response(serializer.data)
  
  
  def create(self, request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  
  def retrieve(self, request, pk=None):
        
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
  
  
  def update(self, request, pk=None):
    category = self.get_object(pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  
  def partial_update(self, request, pk=None):
    category = self.get_object(pk=pk)
    serializer = CategorySerializer(category, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  
  def destroy(self, request, pk=None):
    category = self.get_object(pk=pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ViewSet):
  queryset = Post.objects.all()
  
  def list(self, request):
    serializer = PostSerializer(self.queryset, many=True)
    return Response(serializer.data)
  
  
  def create(self, request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  def retrieve(self, request, pk=None):
    post = get_object_or_404(self.queryset, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
  
  
  def update(self, request, pk=None):
    post = self.get_object(pk=pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  def partial_update(self, request, pk=None):
    post = self.get_object(pk=pk)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  def destroy(self, request, pk=None):
    post = self.get_object(pk=pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  