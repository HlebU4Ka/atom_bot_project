import requests
from django import forms
from django.conf import settings
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext


# Формы для ввода данных

class TelegramNotificationForm(forms.Form):
    user_id = forms.IntegerField()
    massage_text = forms.CharField(widget=forms.Textarea)


def send_massage(user_id, massage_id):
    api_key = settings.TELEGRAM_BOT_API_KEY
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'

    data_from_request = {
        "chat_id": user_id,
        "text": massage_id,
    }

    response = requests.post(url, data=data_from_request)

    if response.status_code == 200:
        return response.json()
    else:
        return None


USER_ID, USER_ID_RECEIVED = range(2)


def start_registration(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f"Привет, {user.first_name}! Для регистрации, пожалуйста, введите ваш user_id.",
        reply_markup=ReplyKeyboardRemove()
    )

    return USER_ID


def receive_user_id(update: Update, context: CallbackContext):
    user_id = update.message.text
    # Здесь вы можете сохранить user_id в базу данных или в профиль пользователя

    update.message.reply_text(
        f"Спасибо! Ваш user_id ({user_id}) был зарегистрирован. Теперь вы можете продолжить использование бота.",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


