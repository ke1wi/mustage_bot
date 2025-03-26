from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Cancel, Row
from aiogram_dialog.widgets.text import Const, Format

from app.bot.dialogs.handlers.expenses.add import (
    amount_uah_handler,
    approve,
    cancel,
    date_handler,
    name_handler,
    today,
)
from app.bot.states.expenses.add import AddExpenses


def get_add_windows():
    name_window = Window(
        Const("Введіть назву витрати:"),
        MessageInput(name_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=AddExpenses.name,
    )
    date_window = Window(
        Const("Введіть дату витрати (dd.mm.YYYY):"),
        Row(
            Button(Const("Сьогодні"), id="today_button", on_click=today),
        ),
        MessageInput(date_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=AddExpenses.date,
    )
    amount_uah_window = Window(
        Const("Введіть суму витрати в UAH:"),
        MessageInput(amount_uah_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=AddExpenses.amount_uah,
    )
    info_window = Window(
        Const("Перевір чи все правильно:\n"),
        Format("Назва витрати: <b>{dialog_data[name]}</b>"),
        Format("Дата: <b>{dialog_data[date]}</b>"),
        Format("Сума: <b>{dialog_data[amount_uah]} UAH</b>"),
        Row(
            Button(Const("Підтвердити ✅"), id="approve", on_click=approve),
            Cancel(Const("Відміна ❌"), on_click=cancel),
        ),
        state=AddExpenses.info,
        parse_mode="HTML",
    )
    return [name_window, date_window, amount_uah_window, info_window]
