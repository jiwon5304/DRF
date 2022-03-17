from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

# 포스팅조회 시 username 응답 1)
# class PostSerializer(serializers.ModelSerializer):
#     username = serializers.ReadOnlyField(source='author.username')

#     class Meta:
#         model = Post
#         fields = [
#             'pk',
#             'username',
#             'message',
#             'created_at',
#             'updated_at',
#         ]
        
# 포스팅조회 시 username 응답 2)
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        
        
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            'pk',
            'author',
            'message',
            'created_at',
            'updated_at',
        ]
