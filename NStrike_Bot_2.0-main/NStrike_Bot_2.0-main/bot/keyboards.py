from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Создание инлайн-клавиатуры с кнопкой "Начать"
start_button = InlineKeyboardButton(text="Начать", web_app=WebAppInfo(url="https://example.com"))
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[start_button]])
