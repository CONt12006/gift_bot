from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def berries_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Клубника 🍓", callback_data="berries_mik_1"),
                InlineKeyboardButton(text="Голубика 🫐", callback_data="berries_mik_2")
            ],
            
            [
                InlineKeyboardButton(text="Малина", callback_data="berries_mik_3"),
                InlineKeyboardButton(text="Виноград 🍇", callback_data="berries_mik_4")
            ],
            [
                InlineKeyboardButton(text="Вишня 🍒", callback_data="berries_mik_5"),
                InlineKeyboardButton(text="Арбуз 🍉", callback_data="berries_mik_6"),
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="berries_mik_7")],
        ],
    )