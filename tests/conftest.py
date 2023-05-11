"""Contains global fixtures for unit tests"""

import discord
import pytest_asyncio
from discord.ext import commands
from discord.ext import test as dpytest

from growlery.cogs import cog_list
from growlery.config import (
    COMMAND_PREFIX,
)


@pytest_asyncio.fixture
async def bot():
    """Creates a bot instance for testing"""

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    _bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

    await _bot._async_setup_hook()  # noqa: SLF001

    for cog in cog_list:
        await _bot.add_cog(cog(_bot))

    dpytest.configure(_bot)

    return _bot


@pytest_asyncio.fixture(autouse=True)
async def cleanup():
    """Performs cleanup after every test, emptying the message queue"""

    yield
    await dpytest.empty_queue()
