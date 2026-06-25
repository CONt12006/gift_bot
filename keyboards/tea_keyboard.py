from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def drink_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Чай ☕️", callback_data="dik_1")],
            [InlineKeyboardButton(text="Кофе <tg-emoji emoji-id='5280914928998303343'>☕️</tg-emoji>", callback_data="dik_2")],
            [InlineKeyboardButton(text="Какао <tg-emoji emoji-id='5364008518812720885'>☕️</tg-emoji>", callback_data="dik_3")],
            [InlineKeyboardButton(text="Назад 🔙", callback_data="dik_4")],
        ],
    )


def tee_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пимс <tg-emoji emoji-id='5323689375882582475'>☕️</tg-emoji>", callback_data="tik_1")],
            [InlineKeyboardButton(text="Домашний <tg-emoji emoji-id='5413847224826215655'>🫖</tg-emoji>", callback_data="tik_2")],
            [InlineKeyboardButton(text="Назад 🔙", callback_data="tik_3")],
        ],
    )


def home_tea_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Чай Greenfield", callback_data="htik_1"),
                InlineKeyboardButton(text="Чай Four seasons Ahmad tea", callback_data="htik_2")
            ],

            [
                InlineKeyboardButton(text="Чай Curtis Манго", callback_data="htik_3"),
                InlineKeyboardButton(text="Чай Royal tea Richard", callback_data="htik_4")
            ],

            [InlineKeyboardButton(text="Чай Tess Pyramid collection", callback_data="htik_5")],
            [InlineKeyboardButton(text="Назад 🔙", callback_data="htik_6")],
        ],
    )


def cofee_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Теплое кофе ♨️", callback_data="cik_1")],
            [InlineKeyboardButton(text="Айс кофе 🧊", callback_data="cik_2")],
            [InlineKeyboardButton(text="Назад 🔙", callback_data="cik_3")],
        ],
    )


def hot_cofee_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Капучино", callback_data="hcik_1")],
            [InlineKeyboardButton(text="Латте", callback_data="hcik_2")],
            [InlineKeyboardButton(text="Раф", callback_data="hcik_3")],
            [InlineKeyboardButton(text="Назад 🔙", callback_data="hcik_4")],
        ],
    )


def ice_cofee_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мокко", callback_data="icik_1")],
            [InlineKeyboardButton(text="Латте", callback_data="icik_2")],
            [InlineKeyboardButton(text="Бамбл", callback_data="icik_2")],
            [InlineKeyboardButton(text="Назад 🔙", callback_data="icik_3")],
        ],
    )

