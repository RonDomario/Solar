from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import pluto_facts
from keyboards.pluto_kb import pluto_keyboard
from PIL import Image
import io
import datetime

pluto = Router()


@pluto.message(Command("pluto"), Cooldown())
async def pluto_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/pluto.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "pluto"), "<b>Pluto</b>", "HTML",
                           reply_markup=pluto_keyboard())


@pluto.callback_query(lambda callback_query: callback_query.data == "pluto_data")
async def callback(call: CallbackQuery):
    data_dict: dict = pluto_facts.get("data", {})
    data_text = "<b>Pluto</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
