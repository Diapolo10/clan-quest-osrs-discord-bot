"""Implements commands for hiscores"""

from __future__ import annotations

import logging
from http import HTTPStatus
from typing import TYPE_CHECKING

from discord.ext import commands
from reactionmenu import ViewButton, ViewMenu  # type: ignore[import]

if TYPE_CHECKING:
    from discord.message import Message

from growlery.config import (
    RUNESCAPE_HISCORES_LITE_URL,
    AccountType,
    AccountTypeName,
)
from growlery.http_request import fetch_page_content
from growlery.table import BossesTable, MinigamesTable, SkillsTable

logger = logging.getLogger(__name__)


class Hiscores(commands.Cog):  # pylint: disable=R0904
    """Hiscores commands"""

    @commands.command('07hs')
    async def default_hiscores(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches default hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.NORMAL, AccountTypeName.NORMAL)

    @commands.command('07hs-im')
    async def ironman_hiscores(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.IRONMAN, AccountTypeName.IRONMAN)

    @commands.command('07hs-hcim')
    async def hardcore_ironman_hiscores(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches hardcore ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.HARDCORE_IRONMAN, AccountTypeName.HARDCORE_IRONMAN)

    @commands.command('07hs-uim')
    async def ultimate_ironman_hiscores(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches ultimate ironman hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.ULTIMATE_IRONMAN, AccountTypeName.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller')
    async def skiller_hiscores(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches skiller hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.SKILLER, AccountTypeName.SKILLER)

    @commands.command('07hs-def')
    async def defence_pure_hiscores(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches 1 Defence hiscores for the given username"""

        await self.reply_with_hiscores(ctx, username, AccountType.DEFENCE_PURE, AccountTypeName.DEFENCE_PURE)

    @commands.command('07hs-minigames')
    async def default_minigames(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches default minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.NORMAL, AccountTypeName.NORMAL)

    @commands.command('07hs-im-minigames')
    async def ironman_minigames(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches ironman minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.IRONMAN, AccountTypeName.IRONMAN)

    @commands.command('07hs-hcim-minigames')
    async def hardcore_ironman_minigames(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches hardcore ironman minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.HARDCORE_IRONMAN, AccountTypeName.HARDCORE_IRONMAN)

    @commands.command('07hs-uim-minigames')
    async def ultimate_ironman_minigames(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches ultimate ironman minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.ULTIMATE_IRONMAN, AccountTypeName.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller-minigames')
    async def skiller_minigames(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches skiller minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.SKILLER, AccountTypeName.SKILLER)

    @commands.command('07hs-def-minigames')
    async def defence_pure_minigames(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches 1 Defence minigame hiscores for the given username"""

        await self.reply_with_minigames(ctx, username, AccountType.DEFENCE_PURE, AccountTypeName.DEFENCE_PURE)

    @commands.command('07hs-bosses')
    async def default_bosses(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches default boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.NORMAL, AccountTypeName.NORMAL)

    @commands.command('07hs-im-bosses')
    async def ironman_bosses(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches ironman boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.IRONMAN, AccountTypeName.IRONMAN)

    @commands.command('07hs-hcim-bosses')
    async def hardcore_ironman_bosses(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches hardcore ironman boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.HARDCORE_IRONMAN, AccountTypeName.HARDCORE_IRONMAN)

    @commands.command('07hs-uim-bosses')
    async def ultimate_ironman_bosses(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches ultimate ironman boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.ULTIMATE_IRONMAN, AccountTypeName.ULTIMATE_IRONMAN)

    @commands.command('07hs-skiller-bosses')
    async def skiller_bosses(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches skiller boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.SKILLER, AccountTypeName.SKILLER)

    @commands.command('07hs-def-bosses')
    async def defence_pure_bosses(self: Hiscores, ctx: commands.Context, *, username: str | None = None) -> None:
        """Fetches 1 Defence boss hiscores for the given username"""

        await self.reply_with_bosses(ctx, username, AccountType.DEFENCE_PURE, AccountTypeName.DEFENCE_PURE)

    @classmethod
    async def reply_with_hiscores(cls: type[Hiscores],
                                  ctx: commands.Context,
                                  username: str | None,
                                  account_type: AccountType,
                                  account_type_name: AccountTypeName) -> Message:
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning(result := "Username assigning to Discord profile not implemented yet.")
            return await ctx.send(result)

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            result = SkillsTable(username, account_type, account_type_name, hiscores).render_table()  # type: ignore[assignment]

        return await ctx.send(result)

    @classmethod
    async def reply_with_minigames(cls: type[Hiscores],
                                   ctx: commands.Context,
                                   username: str | None,
                                   account_type: AccountType,
                                   account_type_name: AccountTypeName) -> Message:
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning(result := "Username assigning to Discord profile not implemented yet.")
            return await ctx.send(result)

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            result = MinigamesTable(username, account_type, account_type_name, hiscores).render_table()  # type: ignore[assignment]

        return await ctx.send(result)

    @classmethod
    async def reply_with_bosses(cls: type[Hiscores],
                                ctx: commands.Context,
                                username: str | None,
                                account_type: AccountType,
                                account_type_name: AccountTypeName) -> Message | None:
        """Replies to the chat with the given username's hiscores"""

        result = "Hiscores not found."

        if username is None:
            logger.warning(result := "Username assigning to Discord profile not implemented yet.")
            return await ctx.send(result)

        hiscores = await cls._fetch_hiscores(username, account_type)
        if hiscores:
            menu = ViewMenu(ctx, menu_type=ViewMenu.TypeText)
            result = BossesTable(username, account_type, account_type_name, hiscores).render_table()  # type: ignore[assignment]
            if isinstance(result, str):
                menu.add_page(content=result)
            else:
                for page in result:
                    menu.add_page(content=page)
            menu.add_button(ViewButton.go_to_first_page())
            menu.add_button(ViewButton.back())
            menu.add_button(ViewButton.next())
            menu.add_button(ViewButton.go_to_last_page())
            return await menu.start()

        return await ctx.send(result)

    @staticmethod
    async def _fetch_hiscores(username: str, account_type: AccountType) -> list[list[str]] | None:
        """Handles fetching the hiscores for RuneScape accounts"""

        url: str = RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=account_type,
            player_name=username,
        )
        status_messages = {
            HTTPStatus.NOT_FOUND: "Could not find player hiscores",
        }

        csv_data = await fetch_page_content(url=url, status_message_override=status_messages)

        return [
            row.split(',')
            for row in csv_data.strip().splitlines()
        ]
