from django.db import models
from settings_app import settings


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Habit(models.Model):
    """
        Модель, представляющая привычку пользователя.

        Поля:
        - user: Внешний ключ на пользователя, который создал привычку.
        - place: Место, связанное с привычкой.
        - time: Время, когда выполняется привычка.
        - action: Описание самой привычки.
        - is_rewarding_habit: Флаг, указывающий, является ли привычка вознаграждением.
        - related_habit: Связь с другой привычкой.
        - frequency: Частота выполнения привычки (по умолчанию 1).
        - reward: Описание вознаграждения за выполнение привычки.
        - time_required: Время, требуемое для выполнения привычки.
        - is_public: Флаг, указывающий, является ли привычка общедоступной.
        - status: Статус привычки.

        Методы:
        - __str__: Возвращает описание привычки в виде строки.

        """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    time = models.TimeField()
    action = models.CharField(max_length=200)
    is_rewarding_habit = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=200)
    time_required = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.action
