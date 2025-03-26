from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Cancel, Row
from aiogram_dialog.widgets.text import Const, Format

from app.bot.dialogs.handlers.report import (
    approve,
    cancel,
    first_date_handler,
    second_date_handler,
    first_today,
    second_today,
)
from app.bot.states.report import Report


def get_report_windows():
    first_date_window = Window(
        Const("Введіть дату початку (dd.mm.YYYY):"),
        Button(Const("Сьогодні"), id="today_button", on_click=first_today),
        MessageInput(first_date_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=Report.first_date,
    )
    second_date_window = Window(
        Const("Введіть дату кінця (dd.mm.YYYY):"),
        Button(Const("Сьогодні"), id="today_button", on_click=second_today),
        MessageInput(second_date_handler),
        Cancel(Const("Відміна ❌"), on_click=cancel),
        state=Report.second_date,
    )
    info_window = Window(
        Const("Звіт буде сформовано:\n"),
        Format("З <b>{dialog_data[start_date]}</b> по <b>{dialog_data[end_date]}</b>"),
        Row(
            Button(Const("Підтвердити ✅"), id="approve", on_click=approve),
            Cancel(Const("Відміна ❌"), on_click=cancel),
        ),
        state=Report.info,
        parse_mode="HTML",
    )
    return [first_date_window, second_date_window, info_window]
