from datetime import date
from decimal import Decimal

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.services.expense_api import ExpenseAPI
from app.services.types.expense import ExpenseCreate
from app.utils.date import check_date, parse_date


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


async def name_handler(
    message: Message,
    button: Button,
    manager: DialogManager,
):
    manager.dialog_data["name"] = message.text
    await manager.next()


async def date_handler(
    message: Message,
    widget,
    manager: DialogManager,
):
    if date := check_date(message.text.strip()):
        manager.dialog_data["data"] = date
        await manager.next()
    else:
        await message.answer("❌ Помилка: Неправильна дата. Введіть дату ще раз.")


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
        await expense_api.add_expense(
            ExpenseCreate(
                name=manager.dialog_data["name"],
                date=parse_date(manager.dialog_data["date"]),
                amount_uah=manager.dialog_data["amount_uah"],
                user_id=manager.event.from_user.id,
            )
        )
    await callback.message.answer(
        f"Витрата __**{manager.dialog_data['name']}**__ успішно записана!",
        parse_mode="MARKDOWN",
    )
    await callback.answer()
    await manager.done()
