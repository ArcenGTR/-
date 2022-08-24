from aiogram import Bot, Dispatcher
import bot_settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token = bot_settings.settings['TOKEN'])
dp = Dispatcher(bot, storage = storage)