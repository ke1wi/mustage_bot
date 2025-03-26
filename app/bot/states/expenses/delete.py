from aiogram.fsm.state import State, StatesGroup


class DeleteExpenses(StatesGroup):
    date = State()
    expense = State()
    info = State()
