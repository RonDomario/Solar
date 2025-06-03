from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def uranus_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="uranus_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
