from create_bot import admins
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery


admin_router = Router()

@admin_router.callback_query(F.data == "swmik") 
async def start_want_main_inline(callback: CallbackQuery): 
    await callback.answer("⚙️ Думаю чтобы-интересного предложить...") 
    await callback.message.answer("⚙️ Настройки")
