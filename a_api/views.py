from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET'])
def profiles(request):
    users = User.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)