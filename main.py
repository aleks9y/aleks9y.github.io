import asyncio
from aiogram import Bot, Dispatcher

from my_fastapi_server.main import app

token = '7520968044:AAHA1Ck-E4oWGvcO1eGsBJf246oEpLaznkg'

from handlers import router

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')





from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://aleks9y.github.io"],  # Укажите ваш сайт
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
