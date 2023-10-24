from django.core.exceptions import ValidationError


def validate_related_habit(value):
    if value.is_rewarding_habit:
        raise ValidationError("Связанная с этой привычкой не может быть вознаграждающей.")


def validate_time_required(value):
    if value > 120:
        raise ValidationError("Требуемое время не может превышать 120 секунд.")


def validate_frequency(value):
    if value < 7:
        raise ValidationError("Периодичность применения привычки не может быть менее 7 дней.")


def validate_rewarding_habit(value):
    if value.reward or value.related_habit:
        raise ValidationError("Вознаграждающая привычка не может иметь вознаграждения или связанной с ней привычки.")


def validate_is_public(value):
    if value and (value.is_rewarding_habit or value.related_habit):
        raise ValidationError("Общественная привычка не может быть вознаграждающей или иметь связанную с ней привычку.")
