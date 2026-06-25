from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def harmful_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Фастфуд 🍟", callback_data="harmful_mik_1"),
                InlineKeyboardButton(text="Снэки 🍿", callback_data="harmful_mik_2")
            ],
            
            [InlineKeyboardButton(text="Назад 🔙", callback_data="harmful_mik_3")],
        ],
    )


def fast_food_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Снэк бокс", callback_data="fast_food_mik_1")],
            [InlineKeyboardButton(text="Картошка фри", callback_data="fast_food_mik_2")],
            [InlineKeyboardButton(text="Нагетсы", callback_data="fast_food_mik_3"),],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="fast_food_mik_4")],
        ],
    )


def snack_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Чипсы", callback_data="snack_mik_1")],
            [InlineKeyboardButton(text="Попкорн", callback_data="snack_mik_2")],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="snack_mik_4")],
        ],
    )


def chips_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Lay`s из печи с лисичками", callback_data="chips_mik_1")],
            [InlineKeyboardButton(text="Lay`s из печи с нежный сыр с зеленью", callback_data="chips_mik_2")],
            [InlineKeyboardButton(text="Начос с сыром", callback_data="chips_mik_3"),],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="chips_mik_4")],
        ],
    )


def popcorn_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сырный", callback_data="popcorn_mik_1")],
            [InlineKeyboardButton(text="Карамельный", callback_data="popcorn_mik_2")],
            [InlineKeyboardButton(text="С солью", callback_data="popcorn_mik_3"),],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="popcorn_mik_4")],
        ],
    )