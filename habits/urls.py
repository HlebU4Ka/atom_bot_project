from django.urls import path
from .views import HabitList, HabitDelete, PlaceCreate

urlpatterns = [
    path('habits/', HabitList.as_view(), name='habit-list'),
    path('habits/<int:pk>/', HabitDelete.as_view(), name='habit-detail'),
    path('places/create/', PlaceCreate.as_view(), name='place-create')
]
