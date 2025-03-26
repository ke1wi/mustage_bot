from aiogram.types import Message

from app.bot.keyboards.main_menu import main_menu_keyboard
from app.bot.messages.help import HELP_MSG


async def help(message: Message) -> None:
    await message.answer(await HELP_MSG.render_async(), reply_markup=await main_menu_keyboard())
