import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from models import Habit

User = get_user_model()

@pytest.mark.django_db
class TestHabitModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_habit(self):
        habit = Habit.objects.create(user=self.user, name='Exercise', frequency='daily')
        self.assertEqual(habit.name, 'Exercise')
        self.assertEqual(habit.frequency, 'daily')


    def test_update_habit(self):
        habit = Habit.objects.create(user=self.user, name='Exercise', frequency='daily')
        habit.name = 'New Exercise'
        habit.save()
        updated_habit = Habit.objects.get(id=habit.id)
        self.assertEqual(updated_habit.name, 'New Exercise')

    def test_delete_habit(self):
        habit = Habit.objects.create(user=self.user, name='Exercise', frequency='daily')
        habit_id = habit.id
        habit.delete()
        with self.assertRaises(Habit.DoesNotExist):
            Habit.objects.get(id=habit_id)
