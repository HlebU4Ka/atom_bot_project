from rest_framework import generics
from rest_framework import permissions
from .models import Habit, Place
from .serializers import HabitSerializer, PublicHabitSerializer, PlaceSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = PageNumberPagination
    """
      Список и создание привычек.

      Это представление позволяет пользователям просматривать свои привычки или создавать новые.

      Атрибуты:
          queryset (QuerySet): Набор привычек, которые будут отображаться в списке.
          serializer_class (Serializer): Класс сериализатора для привычек.
          permission_classes (List[Permission]): Список классов разрешений, необходимых для этого представления.
          pagination_class (Pagination): Класс пагинации для разбиения результатов на страницы.

      Методы:
          perform_create(self, serializer): Выполняет создание привычки и связывает ее с текущим пользователем.
      """

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDelete(generics.RetrieveUpdateAPIView):
    """
       Получение, обновление или удаление привычки.

       Это представление позволяет пользователям получать, обновлять или удалять индивидуальные привычки.

       Атрибуты:
           queryset (QuerySet): Набор привычек, которые могут быть получены, обновлены или удалены.
           serializer_class (Serializer): Класс сериализатора для привычек.
           permission_classes (List[Permission]): Список классов разрешений, необходимых для этого представления.
       """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permissions_class = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class PublicHabitList(generics.ListAPIView):
    """
    Представление для получения списка общедоступных привычек.

    Это представление использует сериализатор PublicHabitSerializer для преобразования
    данных о привычках, которые установлены как общедоступные (is_public=True), в формат JSON.

    Атрибуты:
        - queryset: Запрос к базе данных для получения списка общедоступных привычек.
        - serializer_class: Сериализатор, используемый для преобразования данных модели Habit в JSON-формат.

    Пример использования:
        Для получения списка общедоступных привычек, можно сделать GET-запрос к этому представлению.
        Например:
        GET /api/public-habits/

    Атрибуты класса:
        - queryset: Запрос к базе данных для получения списка общедоступных привычек.
        - serializer_class: Сериализатор, используемый для преобразования данных модели Habit в JSON-формат.
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = PublicHabitSerializer
    pagination_class = PageNumberPagination


class PlaceCreate(generics.CreateAPIView):
    """
    Представление для новых мест.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
