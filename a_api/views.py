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


@api_view(['GET'])
def comments(request):
    all_comments = Comment.objects.all().order_by('-id')
    serializer = CommentSerializer(all_comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PUT', 'PATCH'])
def edit_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment not found'})

    serializer = CommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment not found'})

    comment.delete()
    return Response({'message': 'Comment deleted successfully'})