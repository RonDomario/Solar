from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


def earth_keyboard():
    with open("../facts/earth.json") as file:
        facts = json.load(file)
    data_button = (InlineKeyboardButton(text="Data", callback_data="earth_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb

