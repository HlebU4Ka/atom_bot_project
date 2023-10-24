from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Habit
        fields = ["place", "user", "time", "action", "status", "time_required",
                  'is_rewarding_habit', "related_habit", "frequency", "reward",
                  'time_required']
