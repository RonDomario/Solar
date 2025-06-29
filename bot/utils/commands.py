from aiogram import Bot
from aiogram.types import BotCommand
import logging

logger = logging.getLogger("../logs/bot.log")

all_commands = {"/mercury": "Information about Mercury",
                "/venus": "Information about Venus",
                "/earth": "Information about Earth",
                "/mars": "Information about Mars",
                "/jupiter": "Information about Jupiter",
                "/saturn": "Information about Saturn",
                "/uranus": "Information about Uranus",
                "/neptune": "Information about Neptune",
                "/pluto": "Information about Pluto",
                "/moonphase": "Current phase of the Moon",
                "/newmoon": "Date of the next New Moon",
                "/fullmoon": "Date of the next Full Moon",
                "/moonphaseat": "Phase of the Moon on a set date",
                "/moonphasenext": "Preview of the next phases of the Moon",
                "/apod": "Astronomy Picture of the Day"}


async def setup_commands(bot: Bot):
    menu_commands = [BotCommand(command=c, description=d) for c, d in all_commands.items()]
    try:
        await bot.set_my_commands(menu_commands)
    except Exception as e:
        logger.error(f"Couldn't create bot commands. {type(e).__name__}: {e}")
