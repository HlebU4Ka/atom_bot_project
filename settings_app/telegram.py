import requests
from django import forms
from users.models import CustomUser
from django.conf import settings


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
