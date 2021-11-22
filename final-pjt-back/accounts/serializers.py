from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Userinfo


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class UserAdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userinfo
        fields = ('pk', 'user', 'nickname', 'birth_date', 'context')
        read_only_fields = ('user',)
