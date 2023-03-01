"""Used to launch the bot as a module"""

import discord

from growlery.main import MyBot, AUTH_TOKEN, COMMAND_PREFIX


intents = discord.Intents.default()
intents.message_content = True

bot = MyBot(command_prefix=COMMAND_PREFIX, intents=intents)
bot.run(AUTH_TOKEN)
