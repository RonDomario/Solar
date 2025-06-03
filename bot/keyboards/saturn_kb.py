from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def saturn_keyboard():
    data_button = (InlineKeyboardButton(text="Data", callback_data="saturn_data"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[data_button]])
    return kb
