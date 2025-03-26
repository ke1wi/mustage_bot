from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.callbacks.expenses import (
    AddExpenseCallback,
    DeleteExpenseCallback,
    EditExpenseCallback,
)
from app.bot.callbacks.report import ReportCallback


async def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="➕ Додати витрату", callback_data=AddExpenseCallback().pack()),
        InlineKeyboardButton(
            text="📊 Отримати звіт",
            callback_data=ReportCallback().pack(),
        ),
    )
    builder.row(
        InlineKeyboardButton(
            text="❌ Видалити витрату",
            callback_data=DeleteExpenseCallback().pack(),
        ),
        InlineKeyboardButton(
            text="✏️ Редагувати витрату",
            callback_data=EditExpenseCallback().pack(),
        ),
    )
    return builder.as_markup()
