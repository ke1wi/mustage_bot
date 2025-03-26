from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import (
    Button,
    Cancel,
    Row,
    ScrollingGroup,
    Select,
)
from aiogram_dialog.widgets.text import Const, Format

from app.bot.dialogs.handlers.expenses.delete import (
    approve,
    cancel,
    date_handler,
    expenses_handler,
)
from app.bot.dialogs.handlers.utils import get_dates, get_expenses
from app.bot.states.expenses.delete import DeleteExpenses


def get_delete_windows():
    date_window = Window(
        Const("Виберіть дату, за якою була додана витрата, яку Ви хочете видалити:"),
        ScrollingGroup(
            Select(
                text=Format("{item}"),
                id="date_select",
                item_id_getter=lambda item: item,
                items="dates",
                on_click=date_handler,
            ),
            id="date_select_group",
            width=2,
            height=5,
        ),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=DeleteExpenses.date,
        getter=get_dates,
    )
    expenses_window = Window(
        Const("Вибери витрату, яку хочеш видалити:"),
        ScrollingGroup(
            Select(
                id="expense_select",
                item_id_getter=lambda item: item.id,
                items="expenses",
                text=Format("{item.name}"),
                on_click=expenses_handler,
            ),
            id="expense_select_group",
            width=3,
            height=5,
        ),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=DeleteExpenses.expense,
        getter=get_expenses,
    )
    info_window = Window(
        Const("Впевнений, що хочеш видалити?\n"),
        Row(
            Button(Const("Так ✅"), id="approve", on_click=approve),
            Cancel(Const("Ні ❌"), on_click=cancel),
        ),
        state=DeleteExpenses.info,
        parse_mode="HTML",
    )
    return [date_window, expenses_window, info_window]
