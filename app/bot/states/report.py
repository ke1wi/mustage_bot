from aiogram.fsm.state import State, StatesGroup


class Report(StatesGroup):
    first_date = State()
    second_date = State()
    info = State()
