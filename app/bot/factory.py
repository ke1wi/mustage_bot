from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation
from aiogram_dialog import setup_dialogs

from app.bot.dialogs import (
    add_expense_dialog,
    delete_expense_dialog,
    edit_expense_dialog,
    report_dialog,
)
from app.bot.handlers import router as main_router
from app.settings import settings
from app.utils.commands import set_bot_commands


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    if (await bot.get_webhook_info()).url != settings.WEBHOOK_URL:
        await bot.delete_webhook(drop_pending_updates=True)
        await set_bot_commands(bot)
        await bot.set_webhook(
            settings.WEBHOOK_URL,
            drop_pending_updates=True,
            secret_token=settings.TELEGRAM_SECRET.get_secret_value(),
            allowed_updates=dispatcher.resolve_used_update_types(),
        )


def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
        storage=MemoryStorage(),
    )
    dispatcher.include_routers(
        main_router,
        add_expense_dialog,
        edit_expense_dialog,
        delete_expense_dialog,
        report_dialog,
    )
    dispatcher.startup.register(on_startup)
    setup_dialogs(dispatcher)

    return dispatcher


def create_bot(token: str) -> Bot:
    return Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
