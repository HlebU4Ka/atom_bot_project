from django.contrib.auth import get_user_model
from django.test import TestCase
from settings_app.tasks import schedule_habit_notification

User = get_user_model()


class TestScheduleHabitNotification(TestCase):
    def test_schedule_habit_notification(self, expected_value=None):
        # Создайте тестового пользователя и запустите задачу
        user = User.objects.create_user(username='testuser', password='testpassword')
        schedule_habit_notification.delay(user_id=user.id, habit_id=1)  # Пример параметров

        # Проверьте, что задача выполнена успешно
        # Важно: в реальном приложении вы, возможно, захотите использовать более подходящие методы проверки
        # в зависимости от того, как вы реализуете отправку сообщений в вашем коде.
        # Например, можно проверить, что в базе данных создана запись об отправленном сообщении.
        self.assertEqual(user.some_expected_value, expected_value, "Ожидаемый результат после выполнения задачи")
