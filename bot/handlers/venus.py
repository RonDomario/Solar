from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import venus_facts
from keyboards.venus_kb import venus_keyboard
from PIL import Image
import io
import datetime

venus = Router()


@venus.message(Command("venus"), Cooldown())
async def venus_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/venus.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "venus"), "<b>Venus</b>", "HTML",
                           reply_markup=venus_keyboard())


@venus.callback_query(lambda callback_query: callback_query.data == "venus_data")
async def callback(call: CallbackQuery):
    data_dict: dict = venus_facts.get("data", {})
    data_text = "<b>Venus</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
    await call.answer()
