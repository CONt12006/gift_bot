from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def fruits_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Мандарины 🍊", callback_data="fruits_mik_1"),
                InlineKeyboardButton(text="Апельсины 🍊", callback_data="fruits_mik_2")
            ],
            
            [
                InlineKeyboardButton(text="Бананы 🍌", callback_data="fruits_mik_3"),
                InlineKeyboardButton(text="Персики 🍑", callback_data="fruits_mik_4")
            ],
            [
                InlineKeyboardButton(text="Абрикосы", callback_data="fruits_mik_5"),
                InlineKeyboardButton(text="Ананас 🍍", callback_data="fruits_mik_6"),
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="fruits_mik_7")],
        ],
    )