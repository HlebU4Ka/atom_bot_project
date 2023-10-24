from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserList(generics.ListCreateAPIView):
    """
    Список и создание пользователей.

    Это представление позволяет аутентифицированным пользователям просматривать список пользователей и создавать новых.

    Атрибуты:
        queryset (QuerySet): Набор пользователей, которые будут отображаться в списке.
        serializer_class (Serializer): Класс сериализатора для пользователей.
        permission_classes (List[Permission]): Список классов разрешений, необходимых для доступа к этому представлению.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление или удаление пользователя.

    Это представление позволяет аутентифицированным пользователям получать, обновлять и удалять индивидуальных пользователей.

    Атрибуты:
        queryset (QuerySet): Набор пользователей, которые могут быть получены, обновлены или удалены.
        serializer_class (Serializer): Класс сериализатора для пользователей.
        permission_classes (List[Permission]): Список классов разрешений, необходимых для доступа к этому представлению.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
