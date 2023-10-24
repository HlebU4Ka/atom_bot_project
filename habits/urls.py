from django.urls import path
from .views import HabitList, HabitDelete

urlpatterns = [
    path('habits/', HabitList.as_view(), name='habit-list'),
    path('habits/<int:pk>/', HabitDelete.as_view(), name='habit-detail'),
]
