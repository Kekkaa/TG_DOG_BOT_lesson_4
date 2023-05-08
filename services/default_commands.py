from aiogram import types, Dispatcher

from loader import config



async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Lets start'),
            types.BotCommand('doggie', 'Show me doggie!'),
        ],
        scope=types.BotCommandScopeAllPrivateChats(),
    )
