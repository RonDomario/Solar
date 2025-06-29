from aiogram.filters import Filter
from aiogram.types import Message
import asyncio
import datetime
from .rate_limits import *


class Cooldown(Filter):
    async def __call__(self, msg: Message) -> bool:
        diff = datetime.datetime.now().timestamp() - user_requests.get(msg.from_user.id, 0)
        if diff < REQUEST_COOLDOWN:
            reply = await msg.answer(f"You can use commands in {REQUEST_COOLDOWN - diff:.01f}s")
            await asyncio.sleep(2)
            await reply.delete()
            return False
        else:
            return True
