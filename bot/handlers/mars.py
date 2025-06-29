from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import mars_facts
from keyboards.mars_kb import mars_keyboard
from PIL import Image
import io
import datetime

mars = Router()


@mars.message(Command("mars"), Cooldown())
async def mars_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/mars.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "mars"), "<b>Mars</b>", "HTML",
                           reply_markup=mars_keyboard())


@mars.callback_query(lambda callback_query: callback_query.data == "mars_data")
async def callback(call: CallbackQuery):
    data_dict: dict = mars_facts.get("data", {})
    data_text = "<b>Mars</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
    await call.answer()
