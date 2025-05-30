from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def mars_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="mars_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
