from celery import shared_task
from users.models import CustomUser
from django.conf import settings
from telegram import Bot
from settings_app.celery import Celery

app = Celery('settings_app')


@shared_task
def send_messages_to_users():
    # Получите всех пользователей
    users = CustomUser.objects.all()

    # Инициализируйте бота Telegram
    bot = Bot(token=settings.TELEGRAM_BOT_API_KEY)

    # Отправьте сообщения каждому пользователю
    for user in users:
        chat_id = user.userprofile.telegram_chat_id

        if chat_id:
            message = 'Содержание вашего сообщения'
            bot.send_message(chat_id=chat_id, text=message)


