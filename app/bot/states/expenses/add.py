from aiogram.fsm.state import State, StatesGroup


class AddExpenses(StatesGroup):
    name = State()
    date = State()
    amount_uah = State()
    info = State()
