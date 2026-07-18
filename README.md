<div align="center">

# 🎁 Gift Bot

### Персональный Telegram-ассистент для выбора подарков, еды и приятных сюрпризов

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0?logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-async-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-FSM-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

**Gift Bot** помогает пользователю выбрать желаемое угощение или сюрприз через удобное многоуровневое Telegram-меню. Бот сохраняет историю выборов, формирует персональный топ предпочтений и отправляет ответственным пользователям уведомления о новых желаниях.

</div>

---

## ✨ Возможности

- Интерактивный каталог с inline-клавиатурами и вложенной навигацией.
- Категории еды: сытное, сладкое, фастфуд, снеки, ягоды и фрукты.
- Отправка карточек товаров и медиагрупп с изображениями.
- Автоматическая регистрация пользователей Telegram.
- Сохранение выбранных товаров и количества выборов в PostgreSQL.
- Формирование персонального **топ-5 предпочтений** пользователя.
- Отправка уведомлений администраторам о выбранном товаре или сюрпризе.
- Отдельное главное меню на базе Reply Keyboard.
- Асинхронная работа с Telegram API и базой данных.
- MongoDB-хранилище для FSM-состояний Aiogram.
- Подготовленная инфраструктура для миграций Alembic.
- Запуск MongoDB через Docker Compose.

---

## 🛠 Технологический стек

| Область | Технологии |
|---|---|
| Язык | Python 3.10+ |
| Telegram Bot API | Aiogram 3, long polling |
| Асинхронность | `asyncio`, async handlers |
| Основная БД | PostgreSQL |
| ORM | SQLAlchemy 2.x Async ORM |
| PostgreSQL-драйвер | asyncpg |
| FSM-хранилище | MongoDB, `PyMongoStorage` |
| Миграции | Alembic |
| Конфигурация | python-decouple, `.env` |
| Планировщик | APScheduler — подключён в конфигурации проекта |
| Контейнеризация | Docker Compose |
| Медиа | Локальный каталог изображений, `FSInputFile`, `InputMediaPhoto` |

---

## 🏗 Архитектура

Проект разделён на независимые слои: точка запуска, конфигурация бота, обработчики, клавиатуры, каталог данных и слой работы с БД.

```mermaid
flowchart LR
    U[Пользователь Telegram] --> B[Aiogram Bot]
    B --> R[Routers / Handlers]
    R --> K[Inline и Reply клавиатуры]
    R --> C[Каталог товаров и медиа]
    R --> P[(PostgreSQL)]
    B --> M[(MongoDB FSM)]
    R --> A[Уведомления администраторам]
```

### Поток пользовательского сценария

1. Пользователь запускает бота командой `/start`.
2. Бот регистрирует пользователя в PostgreSQL, если его ещё нет.
3. Пользователь выбирает категорию и конкретный товар через inline-кнопки.
4. Выбор сохраняется в базе, а счётчик товара увеличивается.
5. Администратор получает уведомление с названием и фотографией выбранного товара.
6. На основании истории бот формирует персональный топ предпочтений.

---

## 📁 Структура проекта

```text
gift_bot/
├── alembic/                 # инфраструктура миграций БД
├── data/                    # каталог товаров и переходов меню
│   ├── food.py
│   ├── end_food.py
│   ├── transition_food.py
│   └── Back.py
├── database/
│   ├── database.py          # async engine и фабрика сессий
│   └── models.py            # SQLAlchemy-модели
├── handlers/
│   ├── start.py             # команды и главное меню
│   ├── inline_function.py   # обработка callback-запросов
│   └── connect_admin.py     # административные обработчики
├── keyboards/               # Reply/Inline-клавиатуры
├── photo/                   # изображения товаров и разделов
├── create_bot.py            # Bot, Dispatcher, FSM и конфигурация
├── run_bot.py               # точка запуска приложения
├── docker-compose.yml       # локальная MongoDB
├── alembic.ini
└── requirements.txt
```

---

## 🗄 Модель данных

В PostgreSQL используются три связанные сущности:

```mermaid
erDiagram
    USER ||--o{ PRODUCT : выбирает
    USER ||--o{ FAVORITE : сохраняет

    USER {
        int id PK
        bigint telegram_id UK
        string username
    }

    PRODUCT {
        int id PK
        string name
        int count
        int user_id FK
    }

    FAVORITE {
        int id PK
        string name
        int user_id FK
    }
```

- `User` — Telegram-пользователь.
- `Products` — выбранный товар и количество его выборов.
- `Favorites` — модель для сохранённых предпочтений.
- Связи настроены через `relationship` и каскадное удаление зависимых записей.

---

## 🚀 Локальный запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd gift_bot
```

### 2. Создание виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Для Windows:

```powershell
.venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Проект также использует SQLAlchemy, Alembic и MongoDB FSM storage. Если они ещё не закреплены в `requirements.txt`, установите их отдельно:

```bash
pip install SQLAlchemy alembic pymongo aiohttp-socks
```

### 4. Запуск MongoDB

```bash
docker compose up -d mongodb
```

Проверка контейнера:

```bash
docker compose ps
```

### 5. Подготовка PostgreSQL

Создайте базу данных и укажите асинхронную строку подключения в `.env`:

```env
PG_LINK=postgresql+asyncpg://postgres:password@localhost:5432/gift_bot
```

При запуске приложение создаёт отсутствующие таблицы через:

```python
Base.metadata.create_all()
```

### 6. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
TOKEN=telegram_bot_token
ADMINS=123456789,987654321
PG_LINK=postgresql+asyncpg://postgres:password@localhost:5432/gift_bot
Mongo_bd=mongodb://localhost:27017/gift_bot
```

| Переменная | Назначение |
|---|---|
| `TOKEN` | токен Telegram-бота от BotFather |
| `ADMINS` | Telegram ID администраторов через запятую |
| `PG_LINK` | async URL подключения к PostgreSQL |
| `Mongo_bd` | URL MongoDB для FSM-хранилища |

> `.env` исключён из Git и не должен попадать в репозиторий.

### 7. Настройка прокси

В текущей конфигурации `create_bot.py` используется локальный SOCKS5-прокси:

```python
AiohttpSession(proxy="socks5://127.0.0.1:12334")
```

Если прокси не нужен, замените создание сессии на:

```python
session = AiohttpSession()
```

### 8. Запуск бота

```bash
python run_bot.py
```

---

## 🔐 Безопасность конфигурации

- Токен бота, строки подключения и список администраторов читаются из `.env`.
- `.env`, локальные БД, логи и виртуальные окружения добавлены в `.gitignore`.
- Для пользовательских записей используется уникальный `telegram_id`.
- Повторная регистрация обрабатывается через PostgreSQL `ON CONFLICT DO NOTHING`.
- SQL-запросы формируются через SQLAlchemy, без ручной конкатенации SQL.

---

## 💡 Инженерные решения

- **Полностью асинхронный I/O** — Telegram API и PostgreSQL не блокируют event loop.
- **Router-based структура Aiogram** — обработчики разделены по функциональным зонам.
- **Data-driven каталог** — товары, изображения и переходы задаются словарями, что упрощает расширение меню.
- **Разделение хранилищ** — PostgreSQL отвечает за бизнес-данные, MongoDB — за FSM-состояния.
- **Персонализация** — рейтинг товаров рассчитывается на основании реальных пользовательских выборов.
- **Административные уведомления** — действия пользователя сразу превращаются в прикладной бизнес-сигнал.

---

## 🧭 Возможные улучшения

- Добавить Dockerfile и единый Compose-стек для бота, PostgreSQL и MongoDB.
- Зафиксировать версии всех библиотек в `requirements.txt`.
- Перенести адрес прокси в переменную окружения.
- Завершить настройку Alembic `target_metadata` и хранить схему только через миграции.
- Добавить repository/service-слой между handlers и SQLAlchemy.
- Покрыть обработчики, клавиатуры и работу с БД автоматическими тестами.
- Добавить структурированное логирование и централизованную обработку ошибок.
- Подключить CI для линтинга, тестов и проверки миграций.

---

## 👨‍💻 Что демонстрирует проект

Проект показывает практический опыт работы с:

- асинхронным Python;
- Telegram Bot API и Aiogram 3;
- проектированием многоуровневых пользовательских сценариев;
- PostgreSQL и SQLAlchemy Async ORM;
- реляционными связями и агрегацией пользовательских данных;
- MongoDB как внешним FSM-хранилищем;
- Docker Compose;
- конфигурацией приложения через переменные окружения;
- декомпозицией проекта на handlers, keyboards, data и database modules.

---

<div align="center">

**Сделано с вниманием к пользовательскому опыту и асинхронной архитектуре.**

</div>

