from django.urls import path
from .views import HabitList, HabitDelete, PlaceCreate, PublicHabitList

urlpatterns = [
    path('habits/', HabitList.as_view(), name='habit-list'),
    path('public-habits/', PublicHabitList.as_view(), name='public-habit-list'),
    path('habits/<int:pk>/', HabitDelete.as_view(), name='habit-detail'),
    path('places/create/', PlaceCreate.as_view(), name='place-create')
]
