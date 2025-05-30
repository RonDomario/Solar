from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


def mercury_keyboard():
    with open("../facts/mercury.json") as file:
        facts = json.load(file)
    data_button = (InlineKeyboardButton(text="Data", callback_data="mercury_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb

