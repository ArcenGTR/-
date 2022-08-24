from aiogram import executor
from handlers import *


async def  start_func(_):
    print('Бот онлайн')

#client.client_handlers(dp)
#admin.admin_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = start_func)