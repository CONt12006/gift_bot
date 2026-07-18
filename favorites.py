from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy import select, delete
from database.database import get_session
from database.models import User, Favorites, Products
from data.food import FOODS
from utils.food_utils import get_photo_path
from create_bot import bot, admins
from aiogram.utils.keyboard import InlineKeyboardBuilder


favorites_router = Router()


async def _get_user_id(session, tg_id: int) -> int | None:
    """Получить внутренний id юзера по telegram_id"""
    res = await session.execute(select(User).where(User.telegram_id == tg_id))
    user = res.scalar_one_or_none()
    return user.id if user else None


async def is_favorite(session, user_id: int, food_name: str) -> bool:
    """Проверить, есть ли блюдо в избранном"""
    res = await session.execute(
        select(Favorites).where(
            Favorites.user_id == user_id,
            Favorites.name == food_name,
        )
    )
    return res.scalar_one_or_none() is not None


async def toggle_favorite(session, user_id: int, food_name: str) -> bool:
    """Добавить/убрать из избранного. Возвращает True, если теперь в избранном"""
    existing = await session.execute(
        select(Favorites).where(
            Favorites.user_id == user_id,
            Favorites.name == food_name,
        )
    )
    fav = existing.scalar_one_or_none()

    if fav:
        await session.delete(fav)
        await session.commit()
        return False
    else:
        session.add(Favorites(user_id=user_id, name=food_name))
        await session.commit()
        return True


async def get_user_favorites(session, user_id: int) -> list[Favorites]:
    """Получить все избранные блюда пользователя"""
    res = await session.execute(
        select(Favorites).where(Favorites.user_id == user_id)
    )
    return res.scalars().all()


def _find_food_key_by_name(food_name: str) -> str | None:
    """Найти ключ в FOODS по названию"""
    for key, value in FOODS.items():
        if value.get("name") == food_name:
            return key
    return None


async def send_favorites_list(chat_id: int, tg_id: int):
    """функция отправки списка избранного"""
    async with get_session() as session:
        user_id = await _get_user_id(session, tg_id)
        if user_id is None:
            await bot.send_message(
                chat_id=chat_id,
                text="Сначала нажми /start ✨"
            )
            return

        favs = await get_user_favorites(session, user_id)

    if not favs:
        await bot.send_message(
            chat_id=chat_id,
            text="В избранном пока пусто \n\n"
                 "Нажимай ❤️ на карточках блюд, чтобы добавлять сюда."
        )
        return

    media: list[InputMediaPhoto] = []
    keyboard = []

    for fav in favs:
        photo_path = get_photo_path(fav.name)
        if photo_path:
            media.append(
                InputMediaPhoto(
                    media=FSInputFile(photo_path),
                    caption=fav.name,
                )
            )

        food_key = _find_food_key_by_name(fav.name)
        if food_key:
            keyboard.append([
                InlineKeyboardButton(
                    text=f"✨ Хочу {fav.name}", 
                    callback_data=f"order_fav:{food_key}"
                ),
                InlineKeyboardButton(
                    text="🗑", 
                    callback_data=f"favdel:{food_key}"
                )
            ])

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if media:
        await bot.send_media_group(chat_id=chat_id, media=media)

    await bot.send_message(
        chat_id=chat_id,
        text="⭐️ <b>Твоё избранное</b>\n\n"
             "Нажми на кнопку, чтобы заказать или убрать блюдо:",
        reply_markup=markup,
        parse_mode="HTML",
    )



@favorites_router.callback_query(F.data.startswith("fav:"))
async def toggle_favorite_handler(callback: CallbackQuery):
    """Нажата кнопка 'В избранное' на карточке блюда"""
    food_key = callback.data.split(":", 1)[1]
    food_data = FOODS.get(food_key)

    if not food_data:
        await callback.answer("Блюдо не найдено 😔", show_alert=True)
        return

    food_name = food_data["name"]
    tg_id = callback.from_user.id

    async with get_session() as session:
        user_id = await _get_user_id(session, tg_id)
        if user_id is None:
            await callback.answer("Сначала нажми /start", show_alert=True)
            return

        now_is_fav = await toggle_favorite(session, user_id, food_name)

    heart = "❤️ В избранном" if now_is_fav else "🤍 В избранное"
    builder = InlineKeyboardBuilder()
    builder.button(text=heart, callback_data=f"fav:{food_key}")

    await callback.message.edit_reply_markup(reply_markup=builder.as_markup())
    await callback.answer("Добавлено в избранное ❤️" if now_is_fav else "Убрано из избранного 🤍")


@favorites_router.message(F.text == "Избранное ⭐️")
async def show_favorites(message: Message):
    """Показать список избранного"""
    tg_id = message.from_user.id
    chat_id = message.chat.id
    await send_favorites_list(chat_id, tg_id)


@favorites_router.callback_query(F.data.startswith("favdel:"))
async def remove_favorite_handler(callback: CallbackQuery):
    """Убрать блюдо из избранного"""
    food_key = callback.data.split(":", 1)[1]
    food_data = FOODS.get(food_key)

    if not food_data:
        await callback.answer("Блюдо не найдено 😔", show_alert=True)
        return

    food_name = food_data["name"]
    tg_id = callback.from_user.id

    async with get_session() as session:
        user_id = await _get_user_id(session, tg_id)
        if user_id:
            await session.execute(
                delete(Favorites).where(
                    Favorites.user_id == user_id,
                    Favorites.name == food_name,
                )
            )
            await session.commit()

    await callback.answer(f"❌ {food_name} убрано из избранного")
    await callback.message.delete()
    await send_favorites_list(callback.message.chat.id, tg_id)


@favorites_router.callback_query(F.data.startswith("order_fav:"))
async def order_from_favorites_handler(callback: CallbackQuery):
    """Обработка заказа блюда прямо из списка избранного"""
    food_key = callback.data.split(":", 1)[1]
    food_data = FOODS.get(food_key)

    if not food_data:
        await callback.answer("Блюдо не найдено ", show_alert=True)
        return

    food_name = food_data["name"]
    photo = FSInputFile(food_data["photo"])

    await callback.message.answer("Скоро все будет для самой любимой ")

    for admin in admins:
        await bot.send_photo(
            chat_id=admin,
            photo=photo,
            caption=f"🚨 <b>Важное уведомление: {food_name}</b>",
            parse_mode="HTML",
        )

    async with get_session() as session:
        user_stmt = select(User).where(User.telegram_id == callback.from_user.id)
        user_res = await session.execute(user_stmt)
        user = user_res.scalar_one_or_none()

        if user:
            query = select(Products).where(
                Products.user_id == user.id,
                Products.name == food_name,
            )
            res = await session.execute(query)
            product = res.scalar_one_or_none()

            if product is None:
                product = Products(name=food_name, count=1, user_id=user.id)
                session.add(product)
            else:
                product.count += 1

            await session.commit()

    await callback.answer("Отличный выбор! ✨")