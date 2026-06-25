from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from keyboards.main_keyboard import main_inline_keyboard
from keyboards.tea_keyboard import drink_inline_keyboard
from keyboards.hearty_keyboard import hearty_main_inline_keyboard
from create_bot import bot, admins
from handlers.start import show_main_menu
from data.food import FOODS
from data.Back import Backs
from data.transition_food import transitions
from data.end_food import end_food


inline_router = Router()


@inline_router.callback_query(F.data == "swmik") # Пользователь нажал на "Я хочу.."
async def start_want_main_inline(callback: CallbackQuery): 
    await callback.answer("⚙️ Думаю чтобы-интересного предложить...") 
    await callback.message.edit_reply_markup(reply_markup=main_inline_keyboard())


@inline_router.callback_query(F.data.contains("mik"))
async def handle_mik(callback: CallbackQuery):
    if callback.data in FOODS:
        """Сработает на ЛЮБОЙ callback_data, где есть 'mik'"""
        await callback.answer("⚙️ Организовываю все самое вкусное...")
        await callback.message.answer("Скоро все будет для самой любимой")

        photo = FSInputFile(FOODS[callback.data]["photo"])
        for admin in admins:
            await bot.send_photo(
                    photo = photo,
                    chat_id=admin,
                    caption=f"🚨 <b>Важное уведомление: {FOODS[callback.data]['name']}</b>\n\n",
                    parse_mode="HTML"
                )
        await show_main_menu(
                chat_id=callback.message.chat.id,
                bot=bot,
            )
    elif callback.data in Backs:
        await callback.message.delete()
        await callback.answer("⚙️ Организовываю все самое вкусное...")
        await callback.message.answer("Чего бы тебе хотелось?", reply_markup = Backs[callback.data]())
    elif callback.data in transitions:
        await callback.message.delete()
        await callback.answer("⚙️ Организовываю все самое вкусное...")
        await callback.message.answer("Чего бы тебе хотелось?", reply_markup = transitions[callback.data]())
    elif callback.data in end_food:
        await callback.message.delete()

        photos = end_food[callback.data]["photo"]     

        media = [
            InputMediaPhoto(media=FSInputFile(photo_path))
            for photo_path in photos
        ]

        await callback.answer("⚙️ Думаю чтобы-интересного предложить...") 
        await callback.message.answer_media_group(media=media)
        await callback.message.answer(
            "⚙️ Выбирай, что тебе по душе:",
            reply_markup=end_food[callback.data]["keyboard"]()
        )
