from aiogram_dialog import Dialog

from app.bot.dialogs.windows.expenses import (
    get_add_windows,
    get_delete_windows,
    get_edit_windows,
)
from app.bot.dialogs.windows.report import get_report_windows

add_expense_dialog = Dialog(*get_add_windows())
delete_expense_dialog = Dialog(*get_delete_windows())
edit_expense_dialog = Dialog(*get_edit_windows())
report_dialog = Dialog(*get_report_windows())
