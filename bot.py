import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Bold
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters.command import Command

from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()
dp['started_at'] = datetime.now().strftime("%d.%m.%Y %H:%M")


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я - многофункциональный бот, который умеет много разных штук.\n \n" \
                         "<b>Команды:</b> \n/start" \
                         "\n/info" \
                         "\n/hello", parse_mode='HTML')


# Хэндлер на команду /hello
@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    content = Text(
        "Привет, ",
        Bold(message.from_user.full_name),
        "!\nКак твоё настроение?"
    )

    kb = [
        [
            types.KeyboardButton(text="Хорошо"),
            types.KeyboardButton(text="Плохо")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Только честно)"
    )

    await message.answer(**content.as_kwargs(), reply_markup=keyboard)


# Кнопка "хорошо" в хэндлере /hello
@dp.message(F.text.lower() == "хорошо")
async def good(message: types.Message):

    kb = [
        [
            types.KeyboardButton(text="Да, давай"),
            types.KeyboardButton(text="Пожалуй, не сегодня")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.reply("Прекрасно, могу рассказать тебе анекдот, хочешь?", reply_markup=keyboard)


# Кнопка "плохо" в хэндлере /hello
@dp.message(F.text.lower() == "плохо")
async def bad(message: types.Message):

    kb = [
        [
            types.KeyboardButton(text="Да, давай"),
            types.KeyboardButton(text="Пожалуй, не сегодня")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.reply("Оу, хочешь, я расскажу тебе анекдот?", reply_markup=keyboard)


# Отображение анекдота
@dp.message(F.text.lower() == "да, давай")
async def yes(message: Message):
    content = Text("Какой-то анекдот")

    kb = [
        [
            types.KeyboardButton(text="Давай ещё"),
            types.KeyboardButton(text="Достаточно")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer(**content.as_kwargs(), reply_markup=keyboard)


# Завершение цикла отображения анекдотов до отображения анекдотов
@dp.message(F.text.lower() == "пожалуй, не сегодня")
async def not_today(message: types.Message):
    await message.reply("Хорошо", reply_markup=types.ReplyKeyboardRemove())


# Продолжение цикла отображения анекдотов
@dp.message(F.text.lower() == "давай ещё")
async def more(message: types.Message):
    await yes(message)


# Завершение цикла отображения анекдотов после отображения анекдотов
@dp.message(F.text.lower() == "достаточно")
async def enought(message: Message):
    await message.reply("Хорошо", reply_markup=types.ReplyKeyboardRemove())


# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен: {started_at}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())