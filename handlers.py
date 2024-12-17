from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from kbds import button

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=button)


# @router.message(F.web_app_data)
# async def web_app(message: Message):
#     await message.answer(message.web_app_data.data)
#     print(message.web_app_data.data)
#



@router.message(F.web_app_data)
async def web_app(message: Message):
    # Обрабатываем данные, отправленные пользователем через мини-приложение
    web_data = message.web_app_data.data
    print(f'Полученные данные: {web_data}')

    # Для примера возвращаем полученные данные пользователю
    await message.answer(f'Вы отправили следующие данные: {web_data}')


