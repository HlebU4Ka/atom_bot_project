# Generated by Django 4.2.6 on 2023-11-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_chat_id_customuser_telegram_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='massage_text',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
