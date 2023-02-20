"""Tests hiscores functionality"""

import discord.ext.test as dpytest
import pytest

from growlery.config import (
    COMMAND_PREFIX,
)


@pytest.mark.xfail
@pytest.mark.asyncio
async def test_normal(bot):  # pylint: disable=W0613
    """Tests posting the stats of a regular account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs Ironman-Dia")
    assert dpytest.verify().message().contains("VIEWING STATS FOR IRONMAN-DIA")  # pylint: disable=E1121
