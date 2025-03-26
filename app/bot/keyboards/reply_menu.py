from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def reply_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕ Додати витрату"),
                KeyboardButton(text="📊 Отримати звіт"),
            ],
            [
                KeyboardButton(text="❌ Видалити витрату"),
                KeyboardButton(text="✏️ Редагувати витрату"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
