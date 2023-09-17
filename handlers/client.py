from aiogram import types, Dispatcher
from keyboards.client_kb import kb_client


async def command_start(message : types.Message):
    try:
        await message.answer("Добро пожаловать!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Произошла какая-то ошибка')
        
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    