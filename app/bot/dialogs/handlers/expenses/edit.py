from datetime import date
from decimal import Decimal
from typing import Union
from uuid import UUID

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.services.expense_api import ExpenseAPI
from app.services.types.expense import ExpenseUpdate
from app.utils.date import parse_date


async def cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.answer()
    await callback.message.answer("Відміняю ❌")
    await manager.done()


async def expenses_handler(
    callback: CallbackQuery,
    widget,
    manager: DialogManager,
    expense_id: Union[UUID, str],
):
    manager.dialog_data["expense_id"] = expense_id
    await manager.next()


async def today(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager,
) -> None:
    _date = date.today().strftime("%d.%m.%Y")
    manager.dialog_data["date"] = _date
    await manager.next()


async def name_handler(
    message: Message,
    button: Button,
    manager: DialogManager,
):
    manager.dialog_data["name"] = message.text
    await manager.next()


async def date_handler(
    callback: CallbackQuery,
    widget,
    manager: DialogManager,
    date: str,
):
    manager.dialog_data["date"] = date
    await manager.next()


async def amount_uah_handler(
    message: Message,
    button: Button,
    manager: DialogManager,
):
    if message.text and message.text.isdecimal():
        manager.dialog_data["amount_uah"] = Decimal(message.text)
        await manager.next()
    else:
        await message.answer("❌ Помилка: Схоже що це не число(\nВведи суму ще раз:")


async def approve(callback: CallbackQuery, button: Button, manager: DialogManager):
    async with ExpenseAPI() as expense_api:
        await expense_api.update_expense(
            expense_id=manager.dialog_data["expense_id"],
            data=ExpenseUpdate(
                name=manager.dialog_data["name"],
                date=parse_date(manager.dialog_data["date"]),
                amount_uah=manager.dialog_data["amount_uah"],
            ),
        )
    await callback.message.answer(f"Витрата {manager.dialog_data['name']} успішно записана!")
    await callback.answer()
    await manager.done()
