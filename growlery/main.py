import os

"""Implements the core of the bot"""

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = os.getenv('DISCORD_TOKEN', 'NONEXISTENT')
# GUILD: str = os.getenv('DISCORD_GUILD', 'NONEXISTENT')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    """Message indicating that the bot is online"""

    print(f'{client.user.name} has connected to Discord!')


@bot.command('07hs', help="Prints out the stats of the given OSRS username")  # type: ignore
async def default_hiscores(ctx: commands.Context, username: str | None = None):
    """Prints out the stats of the given OSRS username"""

    print(f"Got username '{username}'!")
    await ctx.send("Hi")

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

client.run(TOKEN)
