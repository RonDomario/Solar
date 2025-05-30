from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


def saturn_keyboard():
    with open("../facts/saturn.json") as file:
        facts = json.load(file)
    data_button = (InlineKeyboardButton(text="Data", callback_data="saturn_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb

