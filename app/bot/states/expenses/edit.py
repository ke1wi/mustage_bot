from aiogram.fsm.state import State, StatesGroup


class EditExpenses(StatesGroup):
    date = State()
    expense = State()
    name = State()
    new_date = State()
    amount_uah = State()
    info = State()
