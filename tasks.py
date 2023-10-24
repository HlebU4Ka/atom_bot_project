from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail


@shared_task
def send_messages_to_users():
    # Получите всех пользователей
    users = User.objects.all()

    # Отправьте сообщения каждому пользователю
    for user in users:
        subject = 'Ваше сообщение'
        message = 'Содержание вашего сообщения'
        from_email = 'email@example.com'
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)
