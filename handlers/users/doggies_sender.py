import os
import requests
from aiogram import types, Bot, Dispatcher
from loader import dp

TOKEN_API = os.getenv('TOKEN')
bot = Bot(token=TOKEN_API)

@dp.message_handler()
async def send_doggy(message: types.Message):
    doggy_response = requests.get('https://random.dog/woof.json').json().get('url')
    if doggy_response.lower().endswith(('jpg', 'jpeg', 'png')):
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=doggy_response
        )
    elif doggy_response.lower().endswith(('mp4', 'gif')):
        await bot.send_video(
            chat_id=message.from_user.id,
            video=doggy_response
        )
    else:
        await message.answer(text="Oh no, something is wrong. Let's try again")
        print('Error')
    await message.delete()


