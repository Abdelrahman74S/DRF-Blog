from rest_framework import serializers
from .models import Post, Comment
from accounts.models import Profile

class AuthorSerailizer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = ['id','username','location','birth_date']
        

class CommentSerializer(serializers.ModelSerializer):
    author =  AuthorSerailizer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerailizer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'comments', 'title', 'description', 'create_at', 'update_at']
        read_only_fields = ['author']

