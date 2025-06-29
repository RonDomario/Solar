from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from utils.filters import Cooldown
from utils.rate_limits import user_requests
from keyboards.moonphase_kb import moonphase_keyboard
from utils.moon import Moonphase
import datetime
import ephem

moonphase = Router()


@moonphase.message(Command("moonphaseat"), Cooldown())
async def moonphase_at(msg: Message):
    user_requests[msg.chat.id] = datetime.datetime.now().timestamp()
    year, month, _ = datetime.datetime.today().timetuple()[:3]
    await msg.answer("Select the date to see the phase of the Moon", reply_markup=moonphase_keyboard(month, year))


@moonphase.callback_query(lambda callback_query: callback_query.data.startswith("moonphase_"))
async def callback(call: CallbackQuery):
    _, command = call.data.split("_", 1)
    if command == "empty":
        await call.answer()
    elif command.startswith("prev_"):
        month, year = map(int, command.split("_")[1:])
        prev_month = 12 if month == 1 else month - 1
        prev_year = year - 1 if month == 1 else year
        await call.message.edit_reply_markup(reply_markup=moonphase_keyboard(prev_month, prev_year))
        await call.answer()
    elif command.startswith("next_"):
        month, year = map(int, command.split("_")[1:])
        next_month = 1 if month == 12 else month + 1
        next_year = year + 1 if month == 12 else year
        await call.message.edit_reply_markup(reply_markup=moonphase_keyboard(next_month, next_year))
        await call.answer()
    else:
        day, month, year = command.split("_")
        date = ephem.Date(f"{year}/{month}/{day}")
        moon = Moonphase(date)
        await call.message.answer(f"On {day:02}/{month:02}/{year} it is:\n{moon}")
        await call.answer()
