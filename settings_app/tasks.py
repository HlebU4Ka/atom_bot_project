from celery import Celery
from datetime import datetime, timedelta
import telebot

app = Celery("celery_task", broker='pyamqp://guest:guest@localhost//')

TELEGRAM_API_TOKEN = "TELEGRAM_BOT_API_KEY"

telebot_instance = telebot.TeleBot(token=TELEGRAM_API_TOKEN)


@app.task
def send_notification(chat_id, message):
    try:
        telebot_instance.send_message(chat_id, message)
        print(f"Уведомление отправлено по адресу {chat_id}")
    except Exception as e:
        print(f"Ошибка отправки по {chat_id}: {str(e)}")


@app.task
def schedule_habit_notification(chat_id, habit, delay_minutes):
    due_time = datetime.utcnow() + timedelta(minutes=delay_minutes)
    message = f"Не забудьте выполнить привычку '{habit}'!"

    send_notification.apply_async(args=[chat_id, message], eta=due_time)
    print(f"Notification scheduled for {due_time} for habit '{habit}'")


# Пример использования задачи для напоминания о привычке
if __name__ == '__main__':
    # Замените 'YOUR_CHAT_ID' на реальный идентификатор чата в Telegram
    chat_id = 'YOUR_CHAT_ID'
    habit_name = 'Утренняя зарядка'
    delay_minutes = 60  # напомнить через 60 минут

    schedule_habit_notification.apply_async(args=[chat_id, habit_name, delay_minutes], countdown=5)
