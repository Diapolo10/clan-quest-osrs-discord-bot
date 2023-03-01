"""Implements commands for hiscores"""

import logging
from http import HTTPStatus

from discord.ext import commands

from growlery.config import (
    AccountType,
    AccountTypeName,
    RUNESCAPE_HISCORES_LITE_URL,
)
from growlery.http_request import fetch_page_content
from growlery.table import SkillsTable, MinigamesTable, BossesTable

logger = logging.getLogger(__name__)


class Hiscores(commands.Cog):  # pylint: disable=R0904
    """Hiscores commands"""

    @commands.command('07hs')
    async def default_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches default hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.NORMAL, AccountTypeName.NORMAL)

    @commands.command('07hs-im')
    async def ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.IRONMAN, AccountTypeName.IRONMAN)

    @commands.command('07hs-hcim')
    async def hardcore_ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches hardcore ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.HARDCORE_IRONMAN, AccountTypeName.HARDCORE_IRONMAN)

    @commands.command('07hs-uim')
    async def ultimate_ironman_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ultimate ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.ULTIMATE_IRONMAN, AccountTypeName.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller')
    async def skiller_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches skiller hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.SKILLER, AccountTypeName.SKILLER)

    @commands.command('07hs-def')
    async def defence_pure_hiscores(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches 1 Defence hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.DEFENCE_PURE, AccountTypeName.DEFENCE_PURE)

    @commands.command('07hs-minigames')
    async def default_minigames(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches default minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.NORMAL, AccountTypeName.NORMAL)

    @commands.command('07hs-im-minigames')
    async def ironman_minigames(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ironman minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.IRONMAN, AccountTypeName.IRONMAN)

    @commands.command('07hs-hcim-minigames')
    async def hardcore_ironman_minigames(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches hardcore ironman minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.HARDCORE_IRONMAN, AccountTypeName.HARDCORE_IRONMAN)

    @commands.command('07hs-uim-minigames')
    async def ultimate_ironman_minigames(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ultimate ironman minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.ULTIMATE_IRONMAN, AccountTypeName.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller-minigames')
    async def skiller_minigames(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches skiller minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.SKILLER, AccountTypeName.SKILLER)

    @commands.command('07hs-def-minigames')
    async def defence_pure_minigames(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches 1 Defence minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.DEFENCE_PURE, AccountTypeName.DEFENCE_PURE)

    @commands.command('07hs-bosses')
    async def default_bosses(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches default boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.NORMAL, AccountTypeName.NORMAL)

    @commands.command('07hs-im-bosses')
    async def ironman_bosses(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ironman boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.IRONMAN, AccountTypeName.IRONMAN)

    @commands.command('07hs-hcim-bosses')
    async def hardcore_ironman_bosses(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches hardcore ironman boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.HARDCORE_IRONMAN, AccountTypeName.HARDCORE_IRONMAN)

    @commands.command('07hs-uim-bosses')
    async def ultimate_ironman_bosses(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches ultimate ironman boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.ULTIMATE_IRONMAN, AccountTypeName.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller-bosses')
    async def skiller_bosses(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches skiller boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.SKILLER, AccountTypeName.SKILLER)

    @commands.command('07hs-def-bosses')
    async def defence_pure_bosses(self, ctx: commands.Context, *, username: str | None = None):
        """Fetches 1 Defence boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.DEFENCE_PURE, AccountTypeName.DEFENCE_PURE)

    @classmethod
    async def reply_with_hiscores(cls,
                                  ctx: commands.Context,
                                  username: str | None,
                                  account_type: AccountType,
                                  account_type_name: AccountTypeName):
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning(result := "Username assigning to Discord profile not implemented yet.")
            return await ctx.send(result)

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            result = SkillsTable(username, account_type, account_type_name, hiscores).render_table()

        await ctx.send(result)

    @classmethod
    async def reply_with_minigames(cls,
                                   ctx: commands.Context,
                                   username: str | None,
                                   account_type: AccountType,
                                   account_type_name: AccountTypeName):
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning(result := "Username assigning to Discord profile not implemented yet.")
            return await ctx.send(result)

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            result = MinigamesTable(username, account_type, account_type_name, hiscores).render_table()

        await ctx.send(result)

    @classmethod
    async def reply_with_bosses(cls,
                                ctx: commands.Context,
                                username: str | None,
                                account_type: AccountType,
                                account_type_name: AccountTypeName):
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning(result := "Username assigning to Discord profile not implemented yet.")
            return await ctx.send(result)

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            result = BossesTable(username, account_type, account_type_name, hiscores).render_table()

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
