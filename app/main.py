from fastapi import FastAPI

# Импортируем настройки проекта из config.py.
from app.core.config import settings

# Устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения указываем атрибут app_title объекта settings.

description = """
Какой то проект, я пока не шарю что тут будет, но скоро узнаю
"""
app = FastAPI(title=settings.app_title,
              description = settings.description)
