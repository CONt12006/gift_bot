from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.main_keyboard import *
from photo import *
from keyboards.main_keyboard import main_inline_keyboard
import asyncio
import logging
from create_bot import bot, admins


start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
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


async def show_main_menu(
    chat_id: int, 
    bot: Bot, 
    ):
    """
    Показывает главное меню.
    
    :param chat_id: ID чата, куда отправить
    :param bot: Экземпляр бота
    """
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

@start_router.message(F.text == "Избранное 📌")
async def cmd_want(message: Message):
    text = (
        "Тут должно быть что-то с бд от пользователя"
    )

    await message.answer(text,parse_mode="HTML")

@start_router.message(F.text == "Топ любимого от бота ❤️")
async def cmd_want(message: Message):
    photo = FSInputFile("photo/want_main_picture.jpg")
    text = (
        "Пока ничего нет, бд скоро будет"
    )

    await message.answer(text,parse_mode="HTML")

