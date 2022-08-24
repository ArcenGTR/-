from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


but_1 = KeyboardButton('Галлерея')
but_2 = KeyboardButton('Кнопка 2')
but_3 = KeyboardButton('Кнопка 3')
start_kb = ReplyKeyboardMarkup(resize_keyboard = True)
start_kb.add(but_1).add(but_2).insert(but_3)

upload_cancel = KeyboardButton('Отмена')
upload_cancel_kb = ReplyKeyboardMarkup(resize_keyboard = True)
upload_cancel_kb.add(upload_cancel)