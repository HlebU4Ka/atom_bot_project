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


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.

    Этот сериализатор используется для создания новых пользователей в системе.
    Он включает в себя поля, необходимые для регистрации, такие как электронная почта, пароль и имя.

    Атрибуты:
        - email (str): Электронная почта пользователя.
        - password (str): Пароль пользователя (только для записи).
        - name (str): Имя пользователя.

    Мета:
        model (CustomUser): Модель, которая используется для создания новых пользователей.
        fields (list): Список полей, которые должны быть включены в сериализацию.

    Методы:
        create(validated_data): Метод для создания нового пользователя на основе переданных данных.
            Принимает словарь validated_data с данными пользователя и создает нового пользователя
            с использованием метода create_user модели CustomUser. Возвращает созданного пользователя.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name']

    def create(self, validated_data):
        """
        Метод для создания нового пользователя.

        Args:
            validated_data (dict): Словарь с данными пользователя, включая электронную почту, пароль и имя.

        Returns:
            CustomUser: Созданный пользователь.
        """
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        return user
