from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import jupiter_facts
from keyboards.jupiter_kb import jupiter_keyboard
from PIL import Image
import io
import datetime

jupiter = Router()


@jupiter.message(Command("jupiter"), Cooldown())
async def jupiter_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/jupiter.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "jupiter"), "<b>Jupiter</b>", "HTML",
                           reply_markup=jupiter_keyboard())


@jupiter.callback_query(lambda callback_query: callback_query.data == "jupiter_data")
async def callback(call: CallbackQuery):
    data_dict: dict = jupiter_facts.get("data", {})
    data_text = "<b>Jupiter</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
    await call.answer()
