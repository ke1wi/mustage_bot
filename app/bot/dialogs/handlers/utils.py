from aiogram_dialog import DialogManager

from app.services.expense_api import ExpenseAPI
from app.services.types.expense import DatesResponse
from app.utils.date import date_for_user, parse_date


async def get_dates(dialog_manager: DialogManager, **kwargs):
    user_id = dialog_manager.event.from_user.id
    async with ExpenseAPI() as expense_api:
        dates = await expense_api.get_expenses_dates(user_id)
        return DatesResponse(dates=list(map(date_for_user, dates.dates)))


async def get_expenses(dialog_manager: DialogManager, **kwargs):
    date: str = dialog_manager.dialog_data["date"]
    async with ExpenseAPI() as expense_api:
        expenses = await expense_api.get_expenses_by_date(
            parse_date(date),
            dialog_manager.event.from_user.id,
        )
        return expenses


async def expense_attr(**kwargs):
    return {
        "attr": [
            ("name", "name"),
            ("date", "date"),
            ("amount_uah", "amount_uah"),
        ]
    }
