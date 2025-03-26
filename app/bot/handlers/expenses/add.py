from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode, StartMode

from app.bot.states.expenses import AddExpenses


async def add_expense(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        AddExpenses.name,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.EDIT,
    )


async def add_expense_cb(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(
        AddExpenses.name,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.EDIT,
    )
    await callback.answer()
