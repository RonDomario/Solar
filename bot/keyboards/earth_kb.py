from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def earth_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="earth_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
