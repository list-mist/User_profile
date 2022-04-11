from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from details.models import Custom

from api.serializers import UserSerializer

@api_view(['GET'])
def api_detail(request):
    try:
        user=User.objects.get(user=request.user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=UserSerializer(user)
        return Response(serializer.data)


