from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from PIL import Image
import io
import datetime

saturn = Router()


@saturn.message(Command("saturn"), Cooldown())
async def saturn_handler(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/saturn.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await msg.answer_photo(BufferedInputFile(buffer.read(), "saturn"), "<b>Saturn</b>", "HTML")
