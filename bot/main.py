import io
import json
import datetime
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile
from aiogram.exceptions import TelegramBadRequest
import requests
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image
from utils.logger import set_logger

logger = set_logger("../logs/bot.log")
from utils.rate_limits import *  # noqa: E402
from utils.config import Config  # noqa: E402
from utils.moon import Moonphase  # noqa: E402
from utils.commands import setup_commands  # noqa: E402
from utils.filters import Cooldown  # noqa: E402
from keyboards.mars_kb import mars_keyboard  # noqa: E402
from handlers.mercury import mercury  # noqa: E402
from handlers.venus import venus  # noqa: E402
from handlers.earth import earth  # noqa: E402
from handlers.mars import mars  # noqa: E402
from handlers.jupiter import jupiter  # noqa: E402
from handlers.saturn import saturn  # noqa: E402


def apod_update():
    today = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d")
    if apod_cache.exists():
        with open(apod_cache, "r") as file:
            cache = json.load(file)
            if cache.get("date") == today:
                return cache
    url = f"https://api.nasa.gov/planetary/apod?api_key={config.nasa_key}"
    response = requests.get(url)
    logger.info(str(response.headers))
    if response.status_code == 200:
        data = response.json()
        with open(apod_cache, "w") as f:
            json.dump(data, f)
        return data
    else:
        return None


load_dotenv()
config = Config()

apod_cache = Path("../cache/apod_cache.json")
bot = Bot(config.tg_token)
dp = Dispatcher()
dp.include_routers(mercury, venus, earth, mars, jupiter, saturn)


@dp.message(Command("venus"), Cooldown())
async def venus(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/venus.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "venus"), caption="<b>Venus</b>",
                         parse_mode="HTML")


@dp.message(Command("earth"), Cooldown())
async def earth(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/earth.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "earth"), caption="<b>Earth</b>",
                         parse_mode="HTML")


@dp.message(Command("mars"), Cooldown())
async def mars(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/mars.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "mars"), caption="<b>Mars</b>",
                         parse_mode="HTML", reply_markup=mars_keyboard())


@dp.message(Command("jupiter"), Cooldown())
async def jupiter(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/jupiter.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "jupiter"), caption="<b>Jupiter</b>",
                         parse_mode="HTML")


@dp.message(Command("saturn"), Cooldown())
async def saturn(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Image.open("../assets/results/saturn.png")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "saturn"), caption="<b>Saturn</b>",
                         parse_mode="HTML")


@dp.message(Command("moonphase"), Cooldown())
async def moonphase(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    m = Moonphase()
    image = m.draw_img()
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "moonphase"), caption=m.__repr__())


@dp.message(Command("apod"), Cooldown())
async def apod(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    data = apod_update()
    if data:
        if data.get("media_type") == "image":
            image = data.get("hdurl")
            caption = (f"<b>{data.get("title")}</b>\n"
                       f"{data.get("date")}, Copyright: {data.get("copyright")}\n\n"
                       f"{data.get("explanation")}")
            try:
                await bot.send_photo(msg.chat.id, image, caption=caption, parse_mode="HTML")
            except TelegramBadRequest:
                await bot.send_message(msg.chat.id, caption, parse_mode="HTML")


async def main():
    await setup_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.info("Bot is active")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Shutting down... ")
