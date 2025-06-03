from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def pluto_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="pluto_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
