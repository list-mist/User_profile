from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from details.models import Custom

from api.serializers import UserSerializer

@api_view(['GET'])
def api_detail(request):
    try:
        user=User.objects.get(username=request.user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=UserSerializer(user)
        return Response(serializer.data)

@api_view(['PUT'])
def api_update(request):
    try:
        user=User.objects.get(username=request.user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="PUT":
        serializer=UserSerializer(user,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="update successfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_update(request):
    try:
        user=User.objects.get(username=request.user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="DELETE":
        operation=user.delete()
        data={}
        if operation:
            data['success']="delete successfully"
        else:
            data['success']="delete failed"
        return Response(data=data)