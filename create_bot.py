from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='5780893340:AAESKISYEhR0_kshZNcGMEPg8YNKvZ97CLM')
dp = Dispatcher(bot, storage=storage)
