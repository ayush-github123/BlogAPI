from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from Post.models import Post, Comment,Tag, Category
from Post.serializers import PostSerializer, CommentSerializer, TagSerializer, CategorySerializer
# Create your views here.


class Postviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def get_queryset(self): # get_­queryset() method is used to filter the data
        user = self.request.user # get the user from the request
        if user.is_authenticated: # if the user is authenticated
            return Post.objects.filter(user=user) # return the posts of the user
        
    
class Commentviewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer): # perform_create() method is used to create a new object
        serializer.save(user = self.request.user)


class Tagviewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class Categoryviewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer