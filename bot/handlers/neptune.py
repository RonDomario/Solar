from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from utils.fact_loader import neptune_facts
from keyboards.neptune_kb import neptune_keyboard
from PIL import Image
import io
import datetime

neptune = Router()


@neptune.message(Command("neptune"), Cooldown())
async def neptune_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/neptune.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "neptune"), "<b>Neptune</b>", "HTML",
                           reply_markup=neptune_keyboard())


@neptune.callback_query(lambda callback_query: callback_query.data == "neptune_data")
async def callback(call: CallbackQuery):
    data_dict: dict = neptune_facts.get("data", {})
    data_text = "<b>Neptune</b>\n"
    for param, (val, mes) in data_dict.items():
        data_text += f"{param}: {val}{mes}\n"
    await call.message.answer(data_text, "HTML")
