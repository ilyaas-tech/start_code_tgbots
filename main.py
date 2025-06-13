from aiogram import Bot, Dispatcher

import asyncio

from app.handlers import router

from app.database.models import async_main

#Импорты____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

async def main():
    bot = Bot(token='7996223006:AAGrbMMSIBnxgIOE0wZzWDYiPcYQyZcWYfw')
    dp = Dispatcher()
    dp.include_router(router)
    await async_main()
    await dp.start_polling(bot)


if __name__ == '__main__':
    print('Бот запущен')
    asyncio.run(main())