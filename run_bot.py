import asyncio
from create_bot import bot, dp, scheduler

from handlers.start import start_router
from handlers.inline_function import inline_router
from handlers.connect_admin import admin_router


async def main():
    dp.include_router(start_router)
    dp.include_router(inline_router)
    dp.include_router(admin_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())