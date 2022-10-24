from fastapi import FastAPI

# Импортируем настройки проекта из config.py.
from app.api.routers import main_router
from app.core.config import settings
from app.api.endpoints.meeting_room import router
# Устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения указываем атрибут app_title объекта settings.

description = """
Какой то проект, я пока не шарю что тут будет, но скоро узнаю
"""
app = FastAPI(title=settings.app_title,
              description = settings.description)

app.include_router(main_router)