from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import UserInfo

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserSerializer(ModelSerializer):
    user_info = SerializerMethodField()

    def get_user_info(self, obj):
        if not UserInfo.objects.filter(
            user=self.context['request'].user
        ).exists():
            create_user_info = UserInfo.objects.create(
                user=self.context['request'].user
            )
            create_user_info.save()
        if self.context['request'].method in ['PATCH', 'UPDATE']:
            return 'done'
        return UserInfo.objects.filter(
            user=self.context['request'].user
        ).values()

    class Meta:
        model = User
        fields = ('username', 'test')
