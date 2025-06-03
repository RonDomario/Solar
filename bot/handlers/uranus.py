from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import uranus_facts
from keyboards.uranus_kb import uranus_keyboard
from PIL import Image
import io
import datetime

uranus = Router()


@uranus.message(Command("uranus"), Cooldown())
async def uranus_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/uranus.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "uranus"), "<b>Uranus</b>", "HTML",
                           reply_markup=uranus_keyboard())


@uranus.callback_query(lambda callback_query: callback_query.data == "uranus_data")
async def callback(call: CallbackQuery):
    data_dict: dict = uranus_facts.get("data", {})
    data_text = "<b>Uranus</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
