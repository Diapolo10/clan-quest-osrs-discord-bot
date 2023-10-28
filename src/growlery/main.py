"""Implements the core of the bot"""

from __future__ import annotations

import logging
import logging.config

import discord
from discord.ext import commands

from growlery.cogs import cog_list
from growlery.config import (
    AUTH_TOKEN,
    COMMAND_PREFIX,
    LOG_CONFIG,
    LOG_FILES,
)

logging.config.fileConfig(LOG_CONFIG, disable_existing_loggers=False, defaults={'logfilename': str(LOG_FILES)})
logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    """Logs events related to the bot"""

    async def on_ready(self: MyBot) -> None:
        """Message indicating that the bot is online"""

        logger.info("Installing cogs...")

        for cog in cog_list:
            await self.add_cog(cog(self))

        logger.info("Logged in as %s", self.user)

    async def on_message(self: MyBot, message: discord.message.Message) -> None:  # pylint: disable=W0221
        """New message detected"""

        if message.author == self.user:
            return

        logger.info("Message from %s: %s", message.author, message.content)

        await self.process_commands(message)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    bot = MyBot(command_prefix=COMMAND_PREFIX, intents=intents)
    bot.run(AUTH_TOKEN)
