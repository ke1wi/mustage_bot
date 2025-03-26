from aiogram.filters.callback_data import CallbackData


class AddExpenseCallback(CallbackData, prefix="add_expense"):
    pass


class DeleteExpenseCallback(CallbackData, prefix="delete_expense"):
    pass


class EditExpenseCallback(CallbackData, prefix="edit_expense"):
    pass
