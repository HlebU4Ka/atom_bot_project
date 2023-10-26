from rest_framework import serializers
from .models import Habit, Place


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Habit
        fields = ["place", "user", "time", "action", "status", "time_required",
                  'is_rewarding_habit', "related_habit", "frequency", "reward",
                  'time_required']


class PublicHabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для общедоступной информации о привычках.

    Этот сериализатор используется для преобразования модели Habit в JSON-подобный формат,
    который содержит общедоступную информацию о привычках, включая идентификатор, пользователя,
    место, время, действие, награду и требуемое время.

    Мета:
        model (Habit): Модель, которая содержит информацию о привычках.
        fields (list): Список полей, которые должны быть включены в сериализацию.

    Пример использования:
        serializer = PublicHabitSerializer(instance=habit)
        serialized_data = serializer.data

    Атрибуты:
        - model (Habit): Модель, используемая для сериализации.
        - fields (list): Список полей, включенных в сериализацию.
    """

    class Meta:
        model = Habit
        fields = ['id', 'user', 'place', 'time', 'action', 'reward', 'time_required']


class PlaceSerializer(serializers.ModelSerializer):
    """
        Сериализатор для создания новых мест.
    """
    class Meta:
        model = Place
        fields = ['name']