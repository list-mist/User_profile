from django.contrib.auth.models import User
from rest_framework import serializers

from details.models import Custom

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']