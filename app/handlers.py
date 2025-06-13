from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb

import app.database.requests as rq

#Импорты____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

router = Router()


#обработчик на комманду старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('<ТЕКСТ>', reply_markup=kb.<НАЗВАНИЕ КЛАВИАТУРЫ>)


#обработчик на текст
@router.message(F.text == '<ТЕКСТ>')
async def catalog(message: Message):
    await message.answer('<ТЕКСТ>', reply_markup=await kb.<НАЗВАНИЕ КЛАВИАТУРЫ>())