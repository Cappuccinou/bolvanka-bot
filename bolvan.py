import asyncio
from aiogram import Bot
import os

TOKEN = os.environ["BOT_TOKEN"]  # или вставь строкой
bot = Bot(token=TOKEN)

async def main():
    updates = await bot.get_updates()
    for update in updates:
        if update.message:
            print("Chat title:", update.message.chat.title)
            print("Chat ID:", update.message.chat.id)
    await bot.session.close()

asyncio.run(main())
