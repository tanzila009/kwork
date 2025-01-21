from aiogram import Router, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = Router()

@main.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", )
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Customer"),
        KeyboardButton(text="Developer"),
    )
    rkb.adjust(2, repeat=True)
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await message.answer(f'Bittasini tanla', reply_markup=rkb)

@main.message(F.text=='Customer')
async def customer_handler(message: Message) -> None:
    await message.answer(f"Sz Customer tanladiz!")

@main.message(F.text=='Developer')
async def customer_handler(message: Message) -> None:
    await message.answer(f"Sz Developer tanladiz!")
