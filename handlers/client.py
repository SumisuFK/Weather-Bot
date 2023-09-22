from aiogram import types, Dispatcher
from keyboards.client_kb import kb_client
from apiley import API_TOKEN
import requests


async def command_start(message : types.Message):
    try:
        await message.answer("Добро пожаловать! \nДля проверки погоды нам требуется узнать ваше местоположение. \nПожалуйста,нажмите на кнопку 'Поделиться местоположением.'", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Произошла какая-то ошибка')

async def handle_location(message: types.Message):
    try:
        lat = message.location.latitude
        lon = message.location.longitude
        params = {"lat" : lat, "lon" : lon, "appid" : API_TOKEN, "units": "metric"}
        response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=params)
        weather = response.json()
        temperature = weather["current"]["temp"]
        await message.answer(f'По вашему местоположению погода составляет: {temperature}°C')
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')
        await message.reply('Произошла ошибка при обработке вашего запроса.')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.message_handler(content_types=['location'])