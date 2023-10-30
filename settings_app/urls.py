"""
URL configuration for settingsapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from habits.views import HabitList, HabitDelete, PublicHabitList
from users.views import UserList, UserDetail, UserRegistrationView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API habits_project",
        default_version='v1',
        description="project to create and consolidate habits",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserList.as_view(), name='user-list'),  # URL-маршруты для пользователей из приложения "users"
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('habits/', HabitList.as_view(), name='habit-list'),  # URL-маршруты для привычек из приложения "habits"
    path('habits/<int:pk>/', HabitDelete.as_view(), name='habit-detail'),
    path('public_habits/', PublicHabitList.as_view(), name='public-habit-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
