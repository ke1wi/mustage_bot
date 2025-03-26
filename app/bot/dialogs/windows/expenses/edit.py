from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (
    Button,
    Cancel,
    Row,
    ScrollingGroup,
    Select,
)
from aiogram_dialog.widgets.text import Const, Format

from app.bot.dialogs.handlers.expenses.edit import (
    amount_uah_handler,
    approve,
    cancel,
    date_handler,
    expenses_handler,
    name_handler,
    today,
)
from app.bot.dialogs.handlers.utils import get_dates, get_expenses
from app.bot.states.expenses.edit import EditExpenses


def get_edit_windows():
    date_window = Window(
        Const("Виберіть дату, за якою була додана витрата, яку Ви хочете виправити:"),
        ScrollingGroup(
            Select(
                text=Format("{item}"),
                id="date_select",
                item_id_getter=lambda item: item,
                items="dates",
                on_click=date_handler,
            ),
            id="data_select_group",
            width=2,
            height=5,
        ),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=EditExpenses.date,
        getter=get_dates,
    )
    expenses_window = Window(
        Const("Вибери витрату, яку хочеш виправити:"),
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
        state=EditExpenses.expense,
        getter=get_expenses,
    )
    name_window = Window(
        Const("Введіть назву витрати:"),
        MessageInput(name_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=EditExpenses.name,
    )
    new_date_window = Window(
        Const("Введіть дату витрати (dd.mm.YYYY):"),
        Row(
            Button(Const("Сьогодні"), id="today_button", on_click=today),
        ),
        MessageInput(date_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=EditExpenses.new_date,
    )
    amount_uah_window = Window(
        Const("Введіть суму витрати в UAH:"),
        MessageInput(amount_uah_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=EditExpenses.amount_uah,
    )
    info_window = Window(
        Const("Перевір чи все правильно:\n"),
        Format("Назва витрати: <b>{dialog_data[name]}</b>"),
        Format("Дата: <b>{dialog_data[date]}</b>"),
        Format("Сума: <b>{dialog_data[amount_uah]}</b>"),
        Row(
            Button(Const("Підтвердити ✅"), id="approve", on_click=approve),
            Cancel(Const("Відміна ❌"), on_click=cancel),
        ),
        state=EditExpenses.info,
        parse_mode="HTML",
    )
    return [
        date_window,
        expenses_window,
        name_window,
        new_date_window,
        amount_uah_window,
        info_window,
    ]
