from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=" Статистика")],
            [KeyboardButton(text=" Настройки")],
            [KeyboardButton(text=" Профиль")]
        ],
        resize_keyboard=True
    )
    return keyboard