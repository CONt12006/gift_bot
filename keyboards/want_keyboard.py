from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile

def main_want_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Вкусняшки и еда 🍰")],
            [KeyboardButton(text="Красота и романтика 💐")],
            [KeyboardButton(text="Забота и помощь 🫂")],
            [KeyboardButton(text="Время и внимание 🌳 ")],
            [KeyboardButton(text="Сюрприз")]
        ],
        resize_keyboard=True
    )
    return keyboard
