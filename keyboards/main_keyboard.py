from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import FSInputFile

def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Я хочу..🎁")],
            [KeyboardButton(text="О боте")]
        ],
        resize_keyboard=True
    )
    return keyboard
