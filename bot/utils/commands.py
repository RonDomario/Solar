from aiogram import Bot
from aiogram.types import BotCommand
import logging

logger = logging.getLogger("../logs/bot.log")

all_commands = {"/mercury": "Mercury",
                "/venus": "Venus",
                "/earth": "Earth",
                "/mars": "Mars",
                "/jupiter": "Jupiter",
                "/saturn": "Saturn",
                "/moonphase": "Current state of the moon",
                "/apod": "Astronomy Picture of the Day"}


async def setup_commands(bot: Bot):
    menu_commands = [BotCommand(command=c, description=d) for c, d in all_commands.items()]
    try:
        await bot.set_my_commands(menu_commands)
    except Exception as e:
        logger.error(f"Couldn't create bot commands. {type(e).__name__}: {e}")
