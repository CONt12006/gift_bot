from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.pymongo import PyMongoStorage 
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.client.session.aiohttp import AiohttpSession

pg_db = (config('PG_LINK'))
Mongo_link = (config('Mongo_bd'))

admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]
session = AiohttpSession(proxy='socks5://127.0.0.1:12334')

bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML), session=session)

storage = PyMongoStorage.from_url(Mongo_link)
dp = Dispatcher(storage = storage)