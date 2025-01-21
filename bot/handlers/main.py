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
    await message.answer(f'Bittasini tanlang', reply_markup=rkb)

@main.message(F.text=='Customer')
async def customer_handler(message: Message) -> None:
    await message.answer(f"Sz Customer tanladiz!")

@main.message(F.text == 'Developer')
async def developer_handler(message: Message) -> None:
    await message.answer("Sz Developer tanladiz!")
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Backend"),
        KeyboardButton(text="Frontend")
    )
    await message.answer("Tanlang:", reply_markup=rkb.as_markup(resize_keyboard=True))

@main.message(F.text=='Backend')
async def backend_handler(message:Message) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Python"),
        KeyboardButton(text="Java"),
        KeyboardButton(text="C++"),
        KeyboardButton(text="JavaScript")
    )
    rkb.adjust(3, repeat=True)
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await message.answer(f"Programmer languages:", reply_markup=rkb)



