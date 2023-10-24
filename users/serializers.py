from rest_framework import serializers

from django.contrib.auth.models import User

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CustomUser.

    Поля:
    - username: Имя пользователя.
    - email: Адрес электронной почты.
    - first_name: Имя пользователя.
    - last_name: Фамилия пользователя.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']