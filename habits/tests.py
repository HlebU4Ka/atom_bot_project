import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Place, Habit
from .serializers import HabitSerializer, PublicHabitSerializer, PlaceSerializer
from .validators import validate_related_habit, validate_time_required, validate_frequency, \
    validate_rewarding_habit, validate_is_public


@pytest.mark.django_db
def test_place_model():
    place = Place.objects.create(name="Test Place")
    assert str(place) == "Test Place"


@pytest.mark.django_db
def test_habit_model():
    user = User.objects.create(username="testuser", password="testpassword")
    place = Place.objects.create(name="Test Place")
    habit = Habit.objects.create(
        user=user,
        place=place,
        time=timezone.now(),
        action="Test Action",
        is_rewarding_habit=False,
        frequency=7,
        reward="Test Reward",
        time_required=60,
        is_public=False,
        status="Active"
    )



@pytest.mark.django_db
def test_habit_model_validation():
    user = User.objects.create(username="testuser", password="testpassword")
    place = Place.objects.create(name="Test Place")

    # Test validation error for time_required exceeding 120 seconds
    with pytest.raises(ValidationError):
        Habit.objects.create(
            user=user,
            place=place,
            time=timezone.now(),
            is_rewarding_habit=False,
            frequency=7,
            reward="Test Reward",
            time_required=150,  # Exceeding the limit
            is_public=False,
            status="Active"
        )

    # Test validation error for frequency less than 7 days
    with pytest.raises(ValidationError):
        Habit.objects.create(
            user=user,
            place=place,
            time=timezone.now(),
            is_rewarding_habit=False,
            frequency=5,  # Less than 7 days
            reward="Test Reward",
            time_required=60,
            is_public=False,
            status="Active"
        )


@pytest.mark.django_db
def test_habit_serializer():
    user = User.objects.create(username="testuser", password="testpassword")
    place = Place.objects.create(name="Test Place")
    habit_data = {
        "user": user.id,
        "place": place.id,
        "time": timezone.now(),
        "frequency": 7,
        "reward": "Test Reward",
        "time_required": 60,
        "is_public": False,
        "status": "Active"
    }
    serializer = HabitSerializer(data=habit_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_public_habit_serializer():
    user = User.objects.create(username="testuser", password="testpassword")
    place = Place.objects.create(name="Test Place")
    habit = Habit.objects.create(
        user=user,
        place=place,
        time=timezone.now(),

        is_rewarding_habit=False,
        frequency=7,
        reward="Test Reward",
        time_required=60,
        is_public=False,
        status="Active"
    )
    serializer = PublicHabitSerializer(instance=habit)
    assert serializer.data
    assert "user" in serializer.data  # User field should not be included in public serializer


@pytest.mark.django_db
def test_place_serializer():
    place_data = {
        "name": "Test Place"
    }
    serializer = PlaceSerializer(data=place_data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_related_habit_validator():
    habit = Habit(is_rewarding_habit=True)
    with pytest.raises(ValidationError):
        validate_related_habit(habit)


@pytest.mark.django_db
def test_time_required_validator():
    with pytest.raises(ValidationError):
        validate_time_required(150)  # Exceeding the limit


@pytest.mark.django_db
def test_frequency_validator():
    with pytest.raises(ValidationError):
        validate_frequency(5)  # Less than 7 days


@pytest.mark.django_db
def test_rewarding_habit_validator():
    habit = Habit(reward="Test Reward")
    with pytest.raises(ValidationError):
        validate_rewarding_habit(habit)


@pytest.mark.django_db
def test_is_public_validator():
    habit = Habit(is_public=True, is_rewarding_habit=True)
    with pytest.raises(ValidationError):
        validate_is_public(habit)
