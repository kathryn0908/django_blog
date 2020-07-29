from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    


