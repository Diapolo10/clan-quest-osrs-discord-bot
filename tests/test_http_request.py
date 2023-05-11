"""Tests hiscores functionality"""

import pytest

from growlery.config import RUNESCAPE_HISCORES_LITE_URL
from growlery.http_request import fetch_page_content


@pytest.mark.asyncio()
async def test_fetch_page_content_default_status():
    """Tests fetching page content with defalt status messages"""

    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode='',
            player_name='Ironman-Dia',
        ),
    )


@pytest.mark.asyncio()
async def test_fetch_page_content_bad_url():
    """Tests error handling"""

    assert not await fetch_page_content(url="http://totallybrokenurlthisshouldnotwork.com")


@pytest.mark.asyncio()
async def test_fetch_page_content_non_ok_status():
    """Tests fetching page content and handing a non-OK status"""

    assert not await fetch_page_content(url="https://httpstat.us/404")
