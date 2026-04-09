from rest_framework import serializers
from django.contrib.auth import get_user_model
from a_home.models import Comment

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'displayname', 'avatar']


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_id', 'body']