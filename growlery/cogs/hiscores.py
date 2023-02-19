"""Implements commands for hiscores"""

import logging
from http import HTTPStatus

from discord.ext import commands

from growlery.config import (
    AccountType,
    RUNESCAPE_HISCORES_LITE_URL,
    SKILL_NAMES,
)
from growlery.http_request import fetch_page_content

logger = logging.getLogger(__name__)


class Hiscores(commands.Cog):
    """Hiscores commands"""

    @commands.command('07hs')
    async def default_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches default hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.NORMAL)

    @commands.command('07hs-im')
    async def ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.IRONMAN)

    @commands.command('07hs-hcim')
    async def hardcore_ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches hardcore ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.HARDCORE_IRONMAN)

    @commands.command('07hs-uim')
    async def ultimate_ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ultimate ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller')
    async def skiller_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches skiller hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.SKILLER)

    @commands.command('07hs-def')
    async def defence_pure_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches 1 Defence hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.DEFENCE_PURE)

    @classmethod
    async def reply_with_hiscores(cls, ctx: commands.Context, username: str | None, account_type: AccountType):
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning("Username assigning to Discord profile not implemented yet")
            raise NotImplementedError("Username assigning not implemented yet")

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            result = await cls._format_table(username, hiscores, account_type)

        await ctx.send(result)

    @staticmethod
    async def _fetch_hiscores(username: str, account_type: AccountType) -> list[list[str]] | None:
        """Handles fetching the hiscores for RuneScape accounts"""

        url: str = RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=account_type,
            player_name=username
        )
        status_messages = {
            HTTPStatus.NOT_FOUND: "Could not find player hiscores",
        }

        csv_data = await fetch_page_content(url=url, status_message_override=status_messages)

        hiscores = [
            row.split(',') for row in csv_data.strip().splitlines()
        ]

        return hiscores

    @staticmethod
    async def _format_table(username: str, hiscores_data: list[list[str]], account_type: AccountType) -> str:
        """Returns a formatted table of OSRS hiscores stats"""

        table_width = 50

        longest = {
            'Skill': 5,
            'Level': 5,
            'Experience': 10,
            'Rank': 4,
        }
        skill_rows = []

        for skill, (rank, level, exp) in zip(SKILL_NAMES, hiscores_data):
            if len(skill) > longest['Skill']:
                longest['Skill'] = len(skill)
            if len(level) > longest['Level']:
                longest['Level'] = len(level)
            if len(exp) > longest['Experience']:
                longest['Experience'] = len(exp)
            if len(rank) > longest['Rank']:
                longest['Rank'] = len(rank)
            skill_rows.append([skill, level, exp, rank])

        for key in ('Experience', 'Rank'):
            comma_count = max((longest[key] - 1) // 3, 0)
            longest[key] += comma_count

        columns = ' | '.join(
            f'{col:^{length}}'
            for col, length in longest.items()
        )

        table_width = len(columns) + 4
        header_text = f"VIEWING STATS FOR {username.replace('_', ' ').upper()}"
        if account_type != AccountType.NORMAL:
            header_text += f" [{account_type.replace('_', ' ').lstrip().upper()}]"
        table_rows = [
            f"╔{'═' * (table_width-2)}╗",
            f"║{header_text:^{table_width-2}}║",
            f"╠{'═' * (table_width-2)}╣",
            f"║ {columns} ║",
            (
                f"╟─{'─' * longest['Skill']}─"
                f"┬─{'─' * longest['Level']}─"
                f"┬─{'─' * longest['Experience']}─"
                f"┬─{'─' * longest['Rank']}─╢"
            ),
        ]

        for skill, level, exp, rank in skill_rows:
            table_rows.append(
                f"║ {skill:<{longest['Skill']}} "
                f"│ {level:>{longest['Level']}} "
                f"│ {int(exp):>{longest['Experience']},} "
                f"│ {int(rank):>{longest['Rank']},} ║"
            )

        table_rows.append(
            f"╚═{'═' * longest['Skill']}═"
            f"╧═{'═' * longest['Level']}═"
            f"╧═{'═' * longest['Experience']}═"
            f"╧═{'═' * longest['Rank']}═╝"
        )

        return '```text\n'+'\n'.join(table_rows)+'\n```'
