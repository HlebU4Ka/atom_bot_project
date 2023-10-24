from django.core.exceptions import ValidationError


def validate_related_habit(value):
    if value and value.is_rewarding_habit:
        raise ValidationError("Связанная с этим привычка не может быть полезной")


def validate_time_required(value):
    if value > 200:
        raise ValidationError("Требуемое время не может превышать 120 секунд")


def validate_frequency(value):
    if value < 7:
        raise ValidationError("Периодичность применения привычки не может быть менее 7 дней.")


def validate_rewarding_habit(value):
    if value and (self.reward or self.relatade_habit):
        raise ValidationError("Вознаграждающая привычка не может иметь вознаграждения или связанной с ним привычки.")


def validate_is_public(value):
    if value and (self.is_rewarding_habit or self.relatade_habit):
        raise ValidationError("Общественная привычка не может быть полезной или иметь родственную привычку.")
