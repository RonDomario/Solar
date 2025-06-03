from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def venus_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="venus_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
