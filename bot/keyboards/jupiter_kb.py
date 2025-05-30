from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


def jupiter_keyboard():
    with open("../facts/jupiter.json") as file:
        facts = json.load(file)
    data_button = (InlineKeyboardButton(text="Data", callback_data="jupiter_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb

