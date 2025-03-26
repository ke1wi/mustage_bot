from datetime import date
from typing import Union
from uuid import UUID

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.services.expense_api import ExpenseAPI


async def cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.answer()
    await callback.message.answer("Відміняю ❌")
    await manager.done()


async def today(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager,
) -> None:
    _date = date.today().strftime("%d.%m.%Y")
    manager.dialog_data["date"] = _date
    await manager.next()


async def date_handler(
    callback: CallbackQuery,
    widget,
    manager: DialogManager,
    date: str,
):
    manager.dialog_data["date"] = date
    await manager.next()


async def expenses_handler(
    callback: CallbackQuery,
    widget,
    manager: DialogManager,
    expense_id: Union[UUID, str],
):
    manager.dialog_data["expense_id"] = expense_id
    await manager.next()


async def approve(callback: CallbackQuery, button: Button, manager: DialogManager):
    async with ExpenseAPI() as expense_api:
        await expense_api.delete_expense(manager.dialog_data["expense_id"])
    await callback.message.answer("Витрата успішно видалена!")
    await callback.answer()
    await manager.done()
