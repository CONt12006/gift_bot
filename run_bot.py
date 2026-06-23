from vkbottle.bot import Bot, Message

bot = Bot("vk1.a.zAHOGvtI4DZ45pnAVPGTFIJ9S182-6lcqY11tPadiNCYLb2Y4-lVJ9xm20xi12BEfKXQ6sHMxk4apRRjooTmOppgcB0MAlEBDy8Niv25Tsdg37PUsGh3aKiTjGJlheNS4C9IMiL6KmeV5zHjZCz9A-udJ50Sa3rA16qUconCwuGGPWn7kSHk64x_q8Uup1-9RP--fsJPmt_94Eq8qTy8Bg")

@bot.on.message(text="начать")
async def start_handler(message: Message):
    await bot.api.messages.send(peer_id=249211675, message=f"Пользователь {message.from_id} написал: {message.text}", random_id=0)
    await message.answer("Привет")

bot.run_forever()