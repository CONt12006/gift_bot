from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Главное меню📋")],
            [KeyboardButton(text="Сюрприз 🎁")],
            [KeyboardButton(text="Топ любимого от бота ❤️")],
            [KeyboardButton(text="Избранное ⭐️")],
            [KeyboardButton(text="О боте ℹ️")]
        ],
        resize_keyboard=True
    )
    return keyboard


def start_want_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Я хочу.. ✨", callback_data="swmik")]
        ],
    )


def main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Сытное 🍕", callback_data="mikbtn_2")
            ],
            
            [
                InlineKeyboardButton(text="Сладкое 🍰", callback_data="mikbtn_3"),
                InlineKeyboardButton(text="Вредное 🍿", callback_data="mikbtn_4")
            ],
            [
                InlineKeyboardButton(text="Ягоды 🍓", callback_data="mikbtn_5"),
                InlineKeyboardButton(text="Фрукты 🍊", callback_data="mikbtn_6")
            ],
        ],
    )