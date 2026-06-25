from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def sweet_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Шоколад 🍫", callback_data="smik_1"),
                InlineKeyboardButton(text="Торт 🍰", callback_data="smik_2")
            ],
            
            [
                InlineKeyboardButton(text="Выпечка 🥐", callback_data="smik_4")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="smik_5")],
        ],
    )


def chocolate_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Milka", callback_data="chocomik_1"),
                InlineKeyboardButton(text="Kinder", callback_data="chocomik_2")
            ],
            
            [
                InlineKeyboardButton(text="Alpen gold", callback_data="chocomik_3"),
                InlineKeyboardButton(text="Ritter sport", callback_data="chocomik_4")
            ],
            [
                InlineKeyboardButton(text="Популярные шоколадки", callback_data="chocomik_5"),
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="chocomik_6")],
        ],
    )


def popular_chocolate_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Snikers", callback_data="pcmik_1"),
                InlineKeyboardButton(text="Twix", callback_data="pcmik_2")
            ],
            
            [
                InlineKeyboardButton(text="Milky Way", callback_data="pcmik_3"),
                InlineKeyboardButton(text="MM`s", callback_data="pcmik_4")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="pcmik_5")],
        ],
    )

def milka_chocolate_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Bubbles молочный", callback_data="mcmik_1"),
                InlineKeyboardButton(text="Bubbles с бананом", callback_data="mcmik_2")
            ],
            
            [
                InlineKeyboardButton(text="Bubbles с капучино", callback_data="mcmik_3"),
                InlineKeyboardButton(text="Caramel", callback_data="mcmik_4")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="mcmik_5")],
        ],
    )


def Alpen_Gold_chocolate_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Max Fun драже-арахис-карамель", callback_data="agcmik_1"),
                InlineKeyboardButton(text="Max Fun с тропическими фруктами и взрывной карамелью", callback_data="agcmik_2")
            ],
            
            [
                InlineKeyboardButton(text="Max Fun со взрывной карамелью-мармеладом-печеньем", callback_data="agcmik_3"),
                InlineKeyboardButton(text="С Oreo", callback_data="agcmik_4")
            ],

            [
                InlineKeyboardButton(text="С капучино", callback_data="agcmik_5"),
                InlineKeyboardButton(text="Соленый арахис и крекер", callback_data="agcmik_6")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="agcmik_7")],
        ],
    )


def Kinder_chocolate_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Kinder Bueno", callback_data="kcmik_1"),
                InlineKeyboardButton(text="Kinder Country", callback_data="kcmik_2")
            ],
            
            [
                InlineKeyboardButton(text="Kinder сюрприз", callback_data="kcmik_3"),
                InlineKeyboardButton(text="Kinder Maxi", callback_data="kcmik_4")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="kcmik_5")],
        ],
    )


def Ritter_sport_chocolate_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ром, изюм, орех", callback_data="rittermik_1"),
                InlineKeyboardButton(text="Марципан", callback_data="rittermik_2")
            ],
            
            [
                InlineKeyboardButton(text="Соленая карамель/шоколадный брауни", callback_data="rittermik_3"),
                InlineKeyboardButton(text="Яркая смородина/нежная малина", callback_data="rittermik_4")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="rittermik_5")],
        ],
    )


def Cake_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Наполеон", callback_data="cake_mik_1"),
                InlineKeyboardButton(text="Медовик", callback_data="cake_mik_2")
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="cake_mik_3")],
        ],
    )


def bakery_main_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Круассан с миндалем", callback_data="bakery_mik_1"),
                InlineKeyboardButton(text="Синнабон", callback_data="bakery_mik_2")
            ],

            [
                InlineKeyboardButton(text="Вафли Яшкино с карамелью", callback_data="bakery_mik_3"),
                InlineKeyboardButton(text="Печенье шарлиз", callback_data="bakery_mik_4")
            ],

            [
                InlineKeyboardButton(text="Маковый рулет", callback_data="bakery_mik_5"),
            ],

            [InlineKeyboardButton(text="Назад 🔙", callback_data="bakery_mik_6")],
        ],
    )
