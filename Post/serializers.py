from rest_framework import serializers
from Post.models import Post,Comment, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Shows the username instead of ID

    class Meta:
        model = Comment
        fields = ['comments', 'created_at', 'user', 'post']



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) # Shows the comments of the post
    # tags = TagSerializer(many=True, read_only=True) # Shows the tags of the post, this line is necessary because we are using a many to many field
    # categories = CategorySerializer(many=False, read_only=True) # Shows the comments of the post, many= False because we are dealing with a single category
    # the above lines are use to show the comments and tags of the post in the post serializer, we can't use the CommentSerializer
    class Meta:
        model = Post
        fields = '__all__'

