import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types
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
    await message.answer("Hello!")


# Хэндлер на команду /hello
@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    content = Text(
        "Привет, ",
        Bold(message.from_user.full_name)
    )
    await message.answer(**content.as_kwargs())


# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен: {started_at}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())