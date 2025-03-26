from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart

from app.bot.callbacks.expenses import (
    AddExpenseCallback,
    DeleteExpenseCallback,
    EditExpenseCallback,
)
from app.bot.handlers.expenses import (
    add_expense,
    add_expense_cb,
    delete_expense,
    delete_expense_cb,
    edit_expense,
    edit_expense_cb,
)
from app.bot.handlers.help import help
from app.bot.handlers.report import get_report
from app.bot.handlers.start import start

router = Router(name=__name__)

router.message.register(start, CommandStart())
router.message.register(help, Command("help"))
router.message.register(add_expense, Command("add_expense"))
router.message.register(delete_expense, Command("delete_expense"))
router.message.register(edit_expense, Command("edit_expense"))
router.message.register(get_report, Command("get_report"))
router.message.register(add_expense, F.text == "➕ Додати витрату")
router.message.register(delete_expense, F.text == "❌ Видалити витрату")
router.message.register(edit_expense, F.text == "✏️ Редагувати витрату")
router.message.register(get_report, F.text == "📊 Отримати звіт")
router.callback_query.register(add_expense_cb, AddExpenseCallback.filter())
router.callback_query.register(delete_expense_cb, DeleteExpenseCallback.filter())
router.callback_query.register(edit_expense_cb, EditExpenseCallback.filter())
