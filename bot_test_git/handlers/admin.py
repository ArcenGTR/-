from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import default
from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()



@dp.message_handler(commands = ['upload'], state = None)
async def photo_upload(message: types.Message):
    await FSMAdmin.photo.set()
    await message.answer('Загрузи картину:', reply_markup = default.upload_cancel_kb)

@dp.message_handler(content_types = ['photo'], state = FSMAdmin.photo)
async def name_upload(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer('Введи название картины:', reply_markup = default.upload_cancel_kb )


@dp.message_handler(state = FSMAdmin.name)
async def desc_upload(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await FSMAdmin.next()
        await message.answer('Введи описание для картины:', reply_markup = default.upload_cancel_kb)

@dp.message_handler(state = FSMAdmin.description)
async def finish_upload(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await message.answer(str(data), reply_markup = ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(state = '*')
async def upload_cancel(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        if await state.get_state() is None:
            return
        await state.finish()
        await message.answer('Хорошо', reply_markup = ReplyKeyboardRemove())




#def admin_handlers(dp: Dispatcher):
#    dp.register_message_handler(photo_upload, commands = ['upload'], state = None)
#    dp.register_message_handler(name_upload, content_types = ['photo'], state = FSMAdmin.photo)
#    dp.register_message_handler(desc_upload, state = FSMAdmin.name)
#    dp.register_message_handler(finish_upload, state = FSMAdmin.description)
#    dp.register_message_handler(upload_cancel, state = '*')