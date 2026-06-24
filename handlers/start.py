from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.main_keyboard import *
from photo import *
from keyboards.want_keyboard import main_want_keyboard



start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    photo = FSInputFile("photo/photo_2026-06-24_03-19-26.jpg")
    text = (
    "<b>✨ Приветствую!</b>\n\n"
    "<blockquote>Я здесь специально для тебя, "
    "чтобы поднять тебе настроение 💫</blockquote>\n\n"
    "Выбирай, что бы тебе сейчас хотелось, "
    "и я уверен — <tg-spoiler>кое-кто скоро тебе порадует 😉</tg-spoiler>"
    )
    await message.answer_photo(photo, caption=text, reply_markup=get_main_keyboard())

@start_router.message(F.text == "О боте")
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

@start_router.message(F.text == "Я хочу..🎁")
async def cmd_want(message: Message):
    photo = FSInputFile("photo/want_main_picture.jpg")
    text = (
        "💭 <i>Чего бы тебе сейчас больше всего хотелось?</i> ✨"
    )

    await message.answer_photo(photo, caption = text, reply_markup= main_want_keyboard(),parse_mode="HTML")