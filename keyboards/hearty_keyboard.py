from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def hearty_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Суши 🍣", callback_data="hmik_1"),
                InlineKeyboardButton(text="Рамен 🍜", callback_data="hmik_2")
            ],
            
            [
                InlineKeyboardButton(text="Хинкали 🥟", callback_data="hmik_3"),
                InlineKeyboardButton(text="Шаурма 🌯", callback_data="hmik_4")
            ],
            [
                InlineKeyboardButton(text="Пицца 🍕", callback_data="hmik_5"),
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="hmik_6")],
        ],
    )