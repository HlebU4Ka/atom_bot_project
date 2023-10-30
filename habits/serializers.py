from rest_framework import serializers
from .models import Habit, Place
from .validators import validate_time_required, validate_frequency, validate_rewarding_habit, \
    validate_is_public


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Habit
        fields = ["place", "user", "time", "action", "status", "time_required",
                  'is_rewarding_habit', "related_habit", "frequency", "reward",
                  'time_required']

    time_required = serializers.IntegerField(validators=[validate_time_required])
    frequency = serializers.IntegerField(validators=[validate_frequency])
    rewarding_habit = serializers.BooleanField(validators=[validate_rewarding_habit])
    is_public = serializers.BooleanField(validators=[validate_is_public])

    def create(self, validated_data):
        return Habit.objects.create(**validated_data)


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
