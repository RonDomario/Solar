from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def neptune_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="neptune_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
