from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def mercury_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="mercury_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
