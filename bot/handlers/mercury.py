from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import mercury_facts
from keyboards.mercury_kb import mercury_keyboard
from PIL import Image
import io
import datetime

mercury = Router()


@mercury.message(Command("mercury"), Cooldown())
async def mercury_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/mercury.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "mercury"), "<b>Mercury</b>", "HTML",
                           reply_markup=mercury_keyboard())


@mercury.callback_query(lambda callback_query: callback_query.data == "mercury_data")
async def callback(call: CallbackQuery):
    data_dict: dict = mercury_facts.get("data", {})
    data_text = "<b>Mercury</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
    await call.answer()
