from datetime import date

from aiogram.types import BufferedInputFile, CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.services.expense_api import ExpenseAPI
from app.utils.date import check_date, parse_date


async def cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.answer()
    await callback.message.answer("Відміняю ❌")
    await manager.done()


async def first_today(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager,
) -> None:
    _date = date.today().strftime("%d.%m.%Y")
    manager.dialog_data["start_date"] = _date
    await manager.next()


async def second_today(
    callback: CallbackQuery,
    button: Button,
    manager: DialogManager,
) -> None:
    _date = date.today().strftime("%d.%m.%Y")
    manager.dialog_data["end_date"] = _date
    await manager.next()


async def first_date_handler(
    message: Message,
    widget,
    manager: DialogManager,
):
    if date := check_date(message.text.strip()):
        manager.dialog_data["start_date"] = parse_date(date)
        await manager.next()
        return
    await message.answer("❌ Помилка: Неправильна дата. Введіть дату ще раз.")


async def second_date_handler(
    message: Message,
    widget,
    manager: DialogManager,
):
    if date := check_date(message.text.strip()):
        end_date = parse_date(date)
        start_date = manager.dialog_data.get("start_date")
    else:
        await message.answer("❌ Помилка: Неправильна дата. Введіть дату ще раз.")
        return

    if start_date and start_date > end_date:
        await message.answer(
            "❌ Помилка: кінцева дата не може бути раніше початкової. Введіть іншу дату."
        )
        return

    manager.dialog_data["end_date"] = end_date
    await manager.next()


async def approve(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.message.answer("⏳ Генерую звіт...")
    async with ExpenseAPI() as expense_api:
        response = await expense_api.get_report(
            start_date=parse_date(manager.dialog_data["start_date"]),
            end_date=parse_date(manager.dialog_data["end_date"]),
            user_id=manager.event.from_user.id,
        )
        await callback.message.answer_document(
            BufferedInputFile(response.content, filename="expenses_report.xlsx")
        )
    await callback.answer()
    await manager.done()
