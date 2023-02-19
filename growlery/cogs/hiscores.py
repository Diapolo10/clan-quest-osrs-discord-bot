"""Implements commands for hiscores"""

import logging
from http import HTTPStatus

import aiohttp
from discord.ext import commands

from growlery.config import (
    RUNESCAPE_HISCORES_LITE_URL, 
    SKILL_NAMES,
)

logger = logging.getLogger(__name__)


class Hiscores(commands.Cog):
    """Hiscores commands"""

    def __init__(self, bot):
        """Initialises the class"""

        self.bot = bot

    @commands.command('07hs')
    async def default_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches default hiscores for the given username"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        mode = ''
        hiscores = await self._fetch_hiscores(username, mode)
        if hiscores:
            result = await self._format_table(username, hiscores)

        await ctx.send(result)

    @commands.command('07hs-im')
    async def ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ironman hiscores for the given username"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        mode = '_ironman'
        hiscores = await self._fetch_hiscores(username, mode)
        if hiscores:
            result = await self._format_table(username, hiscores)

        await ctx.send(result)

    @commands.command('07hs-hcim')
    async def hardcore_ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches hardcore ironman hiscores for the given username"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        mode = '_hardcore'
        hiscores = await self._fetch_hiscores(username, mode)
        if hiscores:
            result = await self._format_table(username, hiscores)

        await ctx.send(result)

    @commands.command('07hs-uim')
    async def ultimate_ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ultimate ironman hiscores for the given username"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        mode = '_ultimate'
        hiscores = await self._fetch_hiscores(username, mode)
        if hiscores:
            result = await self._format_table(username, hiscores)

        await ctx.send(result)

    @commands.command('07hs-skiller')
    async def skiller_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches skiller hiscores for the given username"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        mode = '_skiller'
        hiscores = await self._fetch_hiscores(username, mode)
        if hiscores:
            result = await self._format_table(username, hiscores)

        await ctx.send(result)

    @commands.command('07hs-def')
    async def defence_pure_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches 1 Defence hiscores for the given username"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        mode = '_skiller_defence'
        hiscores = await self._fetch_hiscores(username, mode)
        if hiscores:
            result = await self._format_table(username, hiscores)

        await ctx.send(result)

    @staticmethod
    async def _fetch_hiscores(username: str, account_type: str) -> list[list[str]] | None:
        """Handles fetching the hiscores for RuneScape accounts"""

        hiscores = None
        url: str = RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=account_type,
            player_name=username
        )

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url=url) as request:

                    if request.status == HTTPStatus.OK:
                        csv_data = await request.text()
                        hiscores = [
                            stat for stat in [
                                row.split(',') for row in csv_data.strip().splitlines()
                            ]
                        ]

                    elif request.status == HTTPStatus.NOT_FOUND:
                        logger.error("Could not find player hiscores")

                    else:
                        logger.error(f"[{request.status}] - {request.reason or 'Unidentified problem'}")

            except aiohttp.ClientConnectionError as err:
                logger.error(f"Connection error: {err}")

        return hiscores

    @staticmethod
    async def _format_table(username: str, hiscores_data: list[list[str]]) -> str:
        table_width = 50

        longest = {
            'Skill': 5,
            'Level': 5,
            'Experience': 10,
            'Rank': 4,
        }
        skill_rows = []

        for skill, (rank, level, xp) in zip(SKILL_NAMES, hiscores_data):
            if len(skill) > longest['Skill']:
                longest['Skill'] = len(skill)
            if len(level) > longest['Level']:
                longest['Level'] = len(level)
            if len(xp) > longest['Experience']:
                longest['Experience'] = len(xp)
            if len(rank) > longest['Rank']:
                longest['Rank'] = len(rank)
            skill_rows.append([skill, level, xp, rank])

        for key in ('Experience', 'Rank'):
            comma_count = (longest[key] - 1) // 3
            longest[key] += comma_count if longest[key] > 0 else 0

        columns = ' | '.join(
            f'{col:^{length}}'
            for col, length in longest.items()
        )
        column_row = f"| {columns} |"

        table_width = len(column_row)
        header_text = f"VIEWING STATS FOR {username.upper()}"
        table_header = f"|{header_text:^{table_width-2}}|"
        table_rows = [
            f"|{'=' * (table_width-2)}|",
            table_header,
            f"|{'=' * (table_width-2)}|",
            column_row,
            f"|{'-' * (table_width-2)}|",
        ]

        for skill, level, xp, rank in skill_rows:
            table_rows.append(
                f"| {skill:<{longest['Skill']}} "
                f"| {level:>{longest['Level']}} "
                f"| {int(xp):>{longest['Experience']},} "
                f"| {int(rank):>{longest['Rank']},} |"
            )

        table_rows.append(f"|{'=' * (table_width-2)}|")

        return '```text\n'+'\n'.join(table_rows)+'\n```'
