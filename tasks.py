from celery import shared_task
from users.models import CustomUser
from django.conf import settings
from telegram import Bot
from celery import Celery

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


# def register(update: Update, context: CallbackContext):
#     update.message.reply_text("Давайте начнем процесс регистрации. Введите /cancel, чтобы отменить его.")
#     return start_registration(update, context)
# updater = Updater("YOUR_BOT_TOKEN", use_context=True)
#
# dp = updater.dispatcher
# dp.add_handler(CommandHandler("register", register))
# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler("register", register)],
#     states={
#         USER_ID: [MessageHandler(Filters.text, receive_user_id)],
#     },
#     fallbacks=[],
# )
# dp.add_handler(conv_handler)
#
# updater.start_polling()