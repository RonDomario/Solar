from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import earth_facts
from keyboards.earth_kb import earth_keyboard
from PIL import Image
import io
import datetime

earth = Router()


@earth.message(Command("earth"), Cooldown())
async def earth_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/earth.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "earth"), "<b>Earth</b>", "HTML",
                           reply_markup=earth_keyboard())


@earth.callback_query(lambda callback_query: callback_query.data == "earth_data")
async def callback(call: CallbackQuery):
    data_dict: dict = earth_facts.get("data", {})
    data_text = "<b>Earth</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
    await call.answer()
