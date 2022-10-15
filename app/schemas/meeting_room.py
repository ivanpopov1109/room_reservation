
from typing import Optional

from pydantic import BaseModel, Field


# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным.
    name: str = Field(..., min_length=1, max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.


# Возвращаемую схему унаследуем от MeetingRoomCreate,
# чтобы снова не описывать обязательное поле name.
class MeetingRoomDB(MeetingRoomCreate):
    id: int
#Чтобы FastAPI мог сериализовать объект ORM-модели в схему MeetingRoomDB, нужно указать,
# что схема может принимать на вход объект базы данных, а не только Python-словарь или JSON-объект.Для этого в подклассе Config устанавливается атрибут
    class Config:
        orm_mode = True

