from celery import Celery
import os

from django.conf import settings
from celery import schedules

# Установите переменную DJANGO_SETTINGS_MODULE в файле settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_app.settings')

# Создайте экземпляр Celery
app = Celery('settings_app')

# Загрузите настройки из файла settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически загрузите задачи из всех файлов tasks.py в приложениях Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
