from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Запустити бота або відкрити меню"),
        BotCommand(command="help", description="Як користуватись ботом"),
        BotCommand(command="add_expense", description="Додати витрату"),
        BotCommand(command="get_report", description="Отримати звіт"),
        BotCommand(command="delete_expense", description="Видалити витрату"),
        BotCommand(command="edit_expense", description="Редагувати витрату"),
    ]

    await bot.set_my_commands(commands)
