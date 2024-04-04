from .models import CustomUser
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "_type"]
        extra_kwargs = {"password": {"write_only": True}}
