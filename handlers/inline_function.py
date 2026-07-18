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
from database.models import Products, User, Favorites

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_session
from database.models import User
from sqlalchemy import select
from favorites import is_favorite, _get_user_id
from aiogram.utils.keyboard import InlineKeyboardBuilder


inline_router = Router()


@inline_router.callback_query(F.data == "swmik") # Пользователь нажал на "Я хочу.."
async def start_want_main_inline(callback: CallbackQuery): 
    await callback.answer("⚙️ Думаю чтобы-интересного предложить...") 
    await callback.message.edit_reply_markup(reply_markup=main_inline_keyboard())


@inline_router.callback_query(F.data.contains("mik"))
async def handle_mik(callback: CallbackQuery):
    if callback.data in FOODS:
        await callback.answer("⚙️ Организовываю все самое вкусное...")
        await callback.message.answer("Скоро все будет для самой любимой")

        name_food = FOODS[callback.data]["name"]
        photo = FSInputFile(FOODS[callback.data]["photo"])

        async with get_session() as session:
            user_id = await _get_user_id(session, callback.from_user.id)
            is_fav = await is_favorite(session, user_id, name_food) if user_id else False

        heart = "❤️ В избранном" if is_fav else "🤍 В избранное"
        builder = InlineKeyboardBuilder()
        builder.button(text=heart, callback_data=f"fav:{callback.data}")
        
        await callback.message.answer(
            "💝",
            reply_markup=builder.as_markup()
        )


        for admin in admins:
            await bot.send_photo(
                chat_id=admin,
                photo=photo,
                caption=f"🚨 <b>Важное уведомление: {name_food}</b>",
                parse_mode="HTML",
            )

        async with get_session() as session:
            user_stmt = select(User).where(User.telegram_id == callback.from_user.id)
            user_res = await session.execute(user_stmt)
            user = user_res.scalar_one_or_none()
            
            query = select(Products).where(
                Products.user_id == user.id,
                Products.name == name_food,
            )
            res = await session.execute(query)
            product = res.scalar_one_or_none()

            if product is None:
                product = Products(name=name_food, count=1, user_id=user.id)
                session.add(product)
            else:
                product.count += 1

            await session.commit()

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

    
