from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import settings
from bot.keyboards import inline_kb
import asyncio



bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer_animation( caption="Привет! Добро пожаловать в наше приложение. Нажмите 'Начать', чтобы открыть веб-приложение.", reply_markup=inline_kb)

async def set_default_commands(bot: Bot):
    commands = [
        types.BotCommand(command="start", description="Запустить бота"),
    ]
    await bot.set_my_commands(commands)
    await bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(
        text="Начать", web_app=types.WebAppInfo(url="https://example.com")
    ))

async def start_bot():
    await set_default_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_bot())
