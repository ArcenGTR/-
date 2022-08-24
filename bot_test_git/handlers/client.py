from aiogram import types
from keyboards import default
from aiogram.types import ReplyKeyboardRemove
from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer('Выбери вариант:', reply_markup = default.start_kb)

@dp.message_handler()
async def main_menu(message: types.Message):
    match message.text:
        case 'Галлерея':
            await message.answer("🙈🙈🙈🙈🙈", reply_markup = ReplyKeyboardRemove())


#def client_handlers(dp: Dispatcher):
#    dp.register_message_handler(start_command, commands=['start', 'help'])
#    dp.register_message_handler(main_menu)
