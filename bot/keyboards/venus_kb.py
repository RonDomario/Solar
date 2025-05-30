from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


def venus_keyboard():
    with open("../facts/venus.json") as file:
        facts = json.load(file)
    data_button = (InlineKeyboardButton(text="Data", callback_data="venus_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb

