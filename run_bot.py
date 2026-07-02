import asyncio
from create_bot import bot, dp

from handlers.start import start_router
from handlers.inline_function import inline_router
from handlers.connect_admin import admin_router

from database.database import engine, Base
from database.models import User, Products, Favorites


async def main():
    dp.include_router(start_router)
    dp.include_router(inline_router)
    dp.include_router(admin_router)

    await bot.delete_webhook(drop_pending_updates=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())