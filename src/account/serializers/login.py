from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


class LoginSerializer(AuthTokenSerializer):
    confirm_password = serializers.CharField()
