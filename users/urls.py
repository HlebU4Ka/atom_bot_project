from django.urls import path
from users.views import UserList, UserDetail, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    # Эндпоинты для авторизации
    path('api/token/', obtain_auth_token, name='api_token'),
    # Эндпоинты для списка и деталей пользователей
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    # Эндпоинт для регистрации пользователей
    path('registration/', UserRegistrationView.as_view(), name='user-registration'),
]