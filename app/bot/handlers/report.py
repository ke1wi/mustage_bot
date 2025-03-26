from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, StartMode

from app.bot.states.report import Report


async def get_report(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        Report.first_date,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.EDIT,
    )
