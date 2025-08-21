import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from kitob import TOKEN
from tugma import menyu25, static_reply1, static_reply2

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum! Kitob janrini tanlang:", reply_markup=menyu25
    )


@dp.message(F.text == "fantastik")
async def handler_fantastik(message: Message):
    await message.answer("Fantastika kitoblari:", reply_markup=static_reply1)


@dp.message(F.text == "tarix")
async def handler_tarix(message: Message):
    await message.answer("Tarixiy kitoblar:", reply_markup=static_reply2)


# Fantastika kitoblari
@dp.message(F.text == "Sehrli dunyo")
async def book_sehrli_dunyo(message: Message):
    await message.answer(
        "Sehrli dunyo kitobining havolasi: https://example.com/sehrli-dunyo"
    )


@dp.message(F.text == "Olov qissasi")
async def book_olov_qissasi(message: Message):
    await message.answer(
        "Olov qissasi kitobining havolasi: https://example.com/olov-qissasi"
    )


@dp.message(F.text == "Sehrli shahar")
async def book_sehrli_shahar(message: Message):
    await message.answer(
        "Sehrli shahar kitobining havolasi: https://example.com/sehrli-shahar"
    )


@dp.message(F.text == "Sehrli yo‘llar")
async def book_sehrli_yollar(message: Message):
    await message.answer(
        "Sehrli yo‘llar kitobining havolasi: https://example.com/sehrli-yollar"
    )


@dp.message(F.text == "Sehrgarlar")
async def book_sehrgarlar(message: Message):
    await message.answer(
        "Sehrgarlar kitobining havolasi: https://example.com/sehrgarlar"
    )


@dp.message(F.text == "Sehrli kitob")
async def book_sehrli_kitob(message: Message):
    await message.answer(
        "Sehrli kitob kitobining havolasi: https://example.com/sehrli-kitob"
    )


@dp.message(F.text == "Sehrli qirolicha")
async def book_sehrli_qirolicha(message: Message):
    await message.answer(
        "Sehrli qirolicha kitobining havolasi: https://example.com/sehrli-qirolicha"
    )


@dp.message(F.text == "Sehrli sayohat")
async def book_sehrli_sayohat(message: Message):
    await message.answer(
        "Sehrli sayohat kitobining havolasi: https://example.com/sehrli-sayohat"
    )


@dp.message(F.text == "Sehrli maktab")
async def book_sehrli_maktab(message: Message):
    await message.answer(
        "Sehrli maktab kitobining havolasi: https://example.com/sehrli-maktab"
    )


@dp.message(F.text == "Sehrli voqea")
async def book_sehrli_voqea(message: Message):
    await message.answer(
        "Sehrli voqea kitobining havolasi: https://example.com/sehrli-voqea"
    )


# Tarixiy kitoblar
@dp.message(F.text == "Oʻzbekiston tarixi")
async def book_uzbekiston_tarixi(message: Message):
    await message.answer(
        "Oʻzbekiston tarixi kitobining havolasi: https://example.com/ozbekiston-tarixi"
    )


@dp.message(F.text == "Samarqand sirlari")
async def book_samarqand_sirlari(message: Message):
    await message.answer(
        "Samarqand sirlari kitobining havolasi: https://example.com/samarqand-sirlari"
    )


@dp.message(F.text == "Temur qissasi")
async def book_temur_qissasi(message: Message):
    await message.answer(
        "Temur qissasi kitobining havolasi: https://example.com/temur-qissasi"
    )


@dp.message(F.text == "Xorazm sirlari")
async def book_xorazm_sirlari(message: Message):
    await message.answer(
        "Xorazm sirlari kitobining havolasi: https://example.com/xorazm-sirlari"
    )


@dp.message(F.text == "Shahzoda hikoyalari")
async def book_shahzoda_hikoyalari(message: Message):
    await message.answer(
        "Shahzoda hikoyalari kitobining havolasi: https://example.com/shahzoda-hikoyalari"
    )


@dp.message(F.text == "Qadimiy shaharda")
async def book_qadimiy_shaharda(message: Message):
    await message.answer(
        "Qadimiy shaharda kitobining havolasi: https://example.com/qadimiy-shaharda"
    )


@dp.message(F.text == "Tarixiy roman")
async def book_tarixiy_roman(message: Message):
    await message.answer(
        "Tarixiy roman kitobining havolasi: https://example.com/tarixiy-roman"
    )


@dp.message(F.text == "Oʻtgan kunlar")
async def book_otgan_kunlar(message: Message):
    await message.answer(
        "Oʻtgan kunlar kitobining havolasi: https://example.com/otgan-kunlar"
    )


@dp.message(F.text == "Dastanlar")
async def book_dastanlar(message: Message):
    await message.answer("Dastanlar kitobining havolasi: https://example.com/dastanlar")


@dp.message(F.text == "Buyuk sarkarda")
async def book_buyuk_sarkarda(message: Message):
    await message.answer(
        "Buyuk sarkarda kitobining havolasi: https://example.com/buyuk-sarkarda"
    )


@dp.message(F.text == "Ortga")
async def ortga_handler(message: Message):
    await message.answer("Bosh menyuga qaytdingiz", reply_markup=menyu25)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtadi!")
