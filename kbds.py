from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Регистрация', web_app=WebAppInfo(url='https://aleks9y.github.io/')),
    ]
], resize_keyboard=True)



