# Все классы и функции для асинхронной работы
# находятся в модуле sqlalchemy.ext.asyncio.
#Для работы с SQLAlchemy нужны сессии. Для асинхронной работы сессии создаются при помощи класса AsyncSession. Как и
# при создании обычной сессии, в класс AsyncSession передаётся объект engine:


from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# Создайте базовый класс для будущих моделей:
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker
from app.core.config import settings
from sqlalchemy import Column, Integer


class PreBase:

    @declared_attr
    def __tablename__(cls):
        # Именем таблицы будет название модели в нижнем регистре.
        return cls.__name__.lower()

    # Во все таблицы будет добавлено поле ID.
    id = Column(Integer, primary_key=True)

# В качестве основы для базового класса укажем класс PreBase.
Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)
# Для работы с SQLAlchemy нужны сессии.
async_session = AsyncSession(engine)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)