import asyncio
import os
from aiogram import Bot, Dispatcher

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_messages():
    while True:
        await bot.send_message(CHAT_ID, "/обнять")
        await asyncio.sleep(120)

async def main():
    asyncio.create_task(send_messages())
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
