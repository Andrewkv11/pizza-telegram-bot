from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

bot = Bot(token='5780893340:AAESKISYEhR0_kshZNcGMEPg8YNKvZ97CLM')
dp = Dispatcher(bot)
answ = dict()
# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton1 = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4', url='https://google.com'),\
     InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton1, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))


@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Не Like', callback_data='like_-1'))
@dp.message_handler(commands='test')
async def test_command(message: types.Message):
    await message.answer('За видео про деплой бота', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
executor.start_polling(dp, skip_updates=True)

