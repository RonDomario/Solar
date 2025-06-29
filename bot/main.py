import io
import json
import ephem
import datetime
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile
import requests
from pathlib import Path
from dotenv import load_dotenv
from utils.logger import set_logger

logger = set_logger("../logs/bot.log")
from utils.rate_limits import *  # noqa: E402
from utils.config import Config  # noqa: E402
from utils.moon import Moonphase  # noqa: E402
from utils.commands import setup_commands  # noqa: E402
from utils.filters import Cooldown  # noqa: E402
from handlers.mercury import mercury  # noqa: E402
from handlers.venus import venus  # noqa: E402
from handlers.earth import earth  # noqa: E402
from handlers.mars import mars  # noqa: E402
from handlers.jupiter import jupiter  # noqa: E402
from handlers.saturn import saturn  # noqa: E402
from handlers.uranus import uranus  # noqa: E402
from handlers.neptune import neptune  # noqa: E402
from handlers.pluto import pluto  # noqa: E402
from handlers.moonphase import moonphase  # noqa: E402


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
dp.include_routers(mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto, moonphase)


@dp.message(Command("moonphase"), Cooldown())
async def moonphase(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    m = Moonphase()
    image = m.draw_img()
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "moonphase"), caption=m.__repr__())


@dp.message(Command("newmoon"), Cooldown())
async def moonphase(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    next_new_moon = ephem.next_new_moon(ephem.now())
    year, month, day, hour, minute, second = next_new_moon.tuple()
    await bot.send_message(msg.chat.id, f"Next new moon is on {day:02}/{month:02}/{year} "
                                        f"at {hour:02}:{minute:02}:{round(second):02}")


@dp.message(Command("fullmoon"), Cooldown())
async def moonphase(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    next_new_moon = ephem.next_full_moon(ephem.now())
    year, month, day, hour, minute, second = next_new_moon.tuple()
    await bot.send_message(msg.chat.id, f"Next full moon is on {day:02}/{month:02}/{year} "
                                        f"at {hour:02}:{minute:02}:{round(second):02}")


@dp.message(Command("moonphasenext"), Cooldown())
async def moonphase(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    image = Moonphase.make_gallery()
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    await bot.send_photo(msg.chat.id, BufferedInputFile(buffer.read(), "moonphasenext"))


@dp.message(Command("apod"), Cooldown())
async def apod(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    data = apod_update()
    if data:
        if data.get("media_type") == "image":
            image = data.get("url")
            hdimage = data.get("hdurl")
            copyright_ = data.get("copyright")
            caption = (f"<a href=\"{image}\"><b>{data.get("title")}</b></a> "
                       f"[<a href=\"{hdimage}\">View original image</a>]\n"
                       f"{data.get("date")}, Copyright: {"None" if copyright_ is None else copyright_.strip()}\n\n"
                       f"{data.get("explanation")}")
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
