from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

menyu25 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="fantastik")],
        [KeyboardButton(text="tarix")],
    ],
    resize_keyboard=True,
)

static_reply1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sehrli dunyo")],
        [KeyboardButton(text="Olov qissasi")],
        [KeyboardButton(text="Sehrli shahar")],
        [KeyboardButton(text="Sehrli yo‘llar")],
        [KeyboardButton(text="Sehrgarlar")],
        [KeyboardButton(text="Sehrli kitob")],
        [KeyboardButton(text="Sehrli qirolicha")],
        [KeyboardButton(text="Sehrli sayohat")],
        [KeyboardButton(text="Sehrli maktab")],
        [KeyboardButton(text="Sehrli voqea")],
        [KeyboardButton(text=" Ortga")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Fantastika kitobini tanlang...",
)

static_reply2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Oʻzbekiston tarixi")],
        [KeyboardButton(text="Samarqand sirlari")],
        [KeyboardButton(text="Temur qissasi")],
        [KeyboardButton(text="Xorazm sirlari")],
        [KeyboardButton(text="Shahzoda hikoyalari")],
        [KeyboardButton(text="Qadimiy shaharda")],
        [KeyboardButton(text="Tarixiy roman")],
        [KeyboardButton(text="Oʻtgan kunlar")],
        [KeyboardButton(text="Dastanlar")],
        [KeyboardButton(text="Buyuk sarkarda")],
        [KeyboardButton(text=" Ortga")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Tarixiy kitobni tanlang...",
)
