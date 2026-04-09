from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from a_home.models import Comment
from .serializers import ProfileSerializer, CommentSerializer

User = get_user_model()

@api_view(['GET'])
def profiles(request):
    users = User.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
    