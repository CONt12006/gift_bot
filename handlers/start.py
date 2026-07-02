import os
from pathlib import Path
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command, Filter
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards.main_keyboard import *
from photo import *
from keyboards.main_keyboard import main_inline_keyboard
import asyncio
from create_bot import bot, admins
from database.models import User, Products, Favorites
from database.database import get_session
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from data.food import FOODS

start_router = Router()


def get_photo_path(food_name: str) -> str | None:
    for item in FOODS.values():
        if item.get("name") == food_name:
            path = item.get("photo", "").strip()
            return path if path else None
    return None


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    tg_id = message.from_user.id
    username = message.from_user.username

    async with get_session() as session:
        stmt = insert(User).values(telegram_id = tg_id, username = username)
        stmt = stmt.on_conflict_do_nothing(index_elements=['telegram_id'])
        await session.execute(stmt)
        await session.commit()

    photo = FSInputFile("photo/photo_2026-06-24_03-19-26.jpg")
    text = (
    "<b>✨ Приветствую!</b>\n\n"
    "<blockquote>Я здесь специально для тебя, "
    "чтобы поднять тебе настроение 💫</blockquote>\n\n"
    "Выбирай, что бы тебе сейчас хотелось, "
    "и я уверен — <tg-spoiler>кое-кто скоро тебя порадует 😉</tg-spoiler>"
    )
    await message.answer_photo(photo, caption=text, reply_markup=get_main_keyboard(), parse_mode = "HTML")
    await message.answer(text = "Чего бы тебе хотелось?", reply_markup=start_want_main_inline_keyboard())

@start_router.message(F.text == "О боте ℹ️")
async def about_bot(message:Message):
    photo = FSInputFile("photo/little_princess.jpg")
    text = (
    'Этот бот был создан специально для <b>любимой принцессы</b> 🌸\n\n'
    'Когда у тебя плохое настроение или захочется чего-нибудь — '
    'твой принц сможет <tg-spoiler>почти</tg-spoiler> прочитать твои мысли '
    'и порадовать любимую 💖\n\n'
    'Что бы ты ни нажала и что бы ни выбрала — '
    'твоё желание <b><i>обязательно сбудется</i></b> в тот же миг ✨'
    )

    await message.answer_photo(
        photo=photo, 
        caption=text, 
        parse_mode="HTML" 
    )


async def show_main_menu(chat_id: int, bot: Bot):
    photo = FSInputFile("photo/photo_2026-06-24_03-19-26.jpg")
    
    text = (
        "<b>✨ Приветствую!</b>\n\n"
        "<blockquote>Я здесь специально для тебя, "
        "чтобы поднять тебе настроение 💫</blockquote>\n\n"
        "Выбирай, что бы тебе сейчас хотелось, "
        "и я уверен — <tg-spoiler>кое-кто скоро тебя порадует 😉</tg-spoiler>"
    )
    
    await bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=text,
            reply_markup=get_main_keyboard(),
            parse_mode="HTML"
        )
    
    await bot.send_message(
        chat_id=chat_id,
        text="Чего бы тебе хотелось?",
        reply_markup=start_want_main_inline_keyboard()
    )


@start_router.message(F.text == "Главное меню📋")
async def cmd_main_menu(message: Message, bot: Bot):
    await show_main_menu(
        chat_id=message.chat.id,
        bot=bot,
    )

@start_router.message(F.text == "Сюрприз 🎁")
async def cmd_want(message: Message):
    photo = FSInputFile("photo/stich_surprise.jpg")
    text = (
    "💝 <b>Все самое лучшее — для любимой</b> 💝\n\n"
    "<i>Я что-нибудь придумаю...</i> ✨"
    )

    await message.answer_photo(photo, caption = text, reply_markup= get_main_keyboard(),parse_mode="HTML")
 
    for admin in admins:
        await bot.send_message(
                chat_id=admin,
                text=f"🚨 <b>Важное уведомление: сделай шикарный сюприз для любимой</b>\n\n{text}",
                parse_mode="HTML"
            )


@start_router.message(F.text == "Топ любимого от бота ❤️")
async def cmd_top_from_bot(message: Message):
    tg_id = message.from_user.id

    async with get_session() as session:
        user_stmt = select(User).where(User.telegram_id == tg_id)
        user_res = await session.execute(user_stmt)
        user = user_res.scalar_one_or_none()

        query = (
            select(Products)
            .where(Products.user_id == user.id)
            .order_by(Products.count.desc())
            .limit(5)
        )
        res = await session.execute(query)
        top_products = res.scalars().all()

    if not top_products:
        await message.answer(
            "Вы еще ничего не выбирали, поэтому пока нечего предложить(",
            parse_mode="HTML",
        )
        return

    media: list[InputMediaPhoto] = []
    buttons: list[InlineKeyboardButton] = []

    for product in top_products:
        buttons.append(
            InlineKeyboardButton(
                text=product.name,
                callback_data=f"top_product:{product.id}",
            )
        )

        photo_path = get_photo_path(product.name)
        if photo_path:
            media.append(
                InputMediaPhoto(
                    media=FSInputFile(photo_path),
                    caption=product.name,
                )
            )

    if media:
        await message.answer_media_group(media=media)

    rows = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)

    await message.answer(
        "⚙️ Выбирай, что тебе по душе:",
        reply_markup=keyboard,
    )


@start_router.callback_query(F.data.startswith("top_product:"))
async def favorites_products_admin(callback: CallbackQuery):
    _, product_id_str = callback.data.split(":")
    product_id = int(product_id_str)

    async with get_session() as session:
        stmt = select(Products).where(Products.id == product_id)
        res = await session.execute(stmt)
        product = res.scalar_one_or_none()

    if product is None:
        await callback.answer("Не удалось найти такой продукт в базе 😔", show_alert=True)
        return

    for admin in admins:
        await bot.send_message(
            chat_id=admin,
            text=(
                f"🚨 Важное уведомление\n\n"
                f"Пользователь @{callback.from_user.username or callback.from_user.id} "
                f"выбрал еду: <b>{product.name}</b>\n"
                f"ID продукта: {product.id}"
            ),
            parse_mode="HTML",
        )

    await callback.message.answer(
        "Скоро всё будет для самой любимой 💝",
        parse_mode="HTML",
    )
    await callback.answer()