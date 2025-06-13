from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import <функции>

#Импорты____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#клавиатура бота
<НАЗВАНИЕ КЛАВИАТУРЫ> = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='<ТЕКСТ>')],
    [KeyboardButton(text='<ТЕКСТ>')],
    [KeyboardButton(text='<ТЕКСТ>'), KeyboardButton(text='<ТЕКСТ>')]],
    resize_keyboard=True
)