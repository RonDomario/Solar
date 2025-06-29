from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from math import ceil as mceil
from calendar import monthrange, month_name


def moonphase_keyboard(month, year):
    weekday_start, num_of_days = monthrange(year, month)
    rows_required = mceil((num_of_days + weekday_start) / 7)
    calendar = []
    prev_button = InlineKeyboardButton(text="<-", callback_data=f"moonphase_prev_{month}_{year}")
    month_label = InlineKeyboardButton(text=f"{month_name[month]} {year}", callback_data="moonphase_empty")
    next_button = InlineKeyboardButton(text="->", callback_data=f"moonphase_next_{month}_{year}")
    header = [prev_button, month_label, next_button]
    calendar.append(header)
    empty = weekday_start
    day = 1
    for row in range(rows_required):
        calendar_row = []
        for dotw in range(7):
            if empty > 0:
                cell = InlineKeyboardButton(text=" ", callback_data="moonphase_empty")
                empty -= 1
            elif day <= num_of_days:
                cell = InlineKeyboardButton(text=f"{day}", callback_data=f"moonphase_{day}_{month}_{year}")
                day += 1
            else:
                cell = InlineKeyboardButton(text=" ", callback_data="moonphase_empty")
            calendar_row.append(cell)
        calendar.append(calendar_row)
    kb = InlineKeyboardMarkup(inline_keyboard=calendar)
    return kb
