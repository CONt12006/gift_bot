from create_bot import pg_db
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager



# Создаём движок (пул соединений)
engine = create_async_engine(
    pg_db,                   # ссылка на бд
    echo=False,              # True — логировать SQL 
    pool_size=10,            # Постоянных соединений в пуле
    max_overflow=20,         # Доп. соединений при пике
    pool_timeout=30,         # Таймаут ожидания свободного соединения
    pool_recycle=1800,       # Пересоздавать соединения каждые 30 мин
    pool_pre_ping=True,      # Проверять "живость" перед использованием
)

# Фабрика сессий
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=True,  # Объекты "протухают" после commit
)


class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""
    pass

@asynccontextmanager
async def get_session():
    """Получить сессию"""
    async with async_session() as session:
        yield session