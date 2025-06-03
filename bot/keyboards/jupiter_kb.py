from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def jupiter_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="jupiter_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
