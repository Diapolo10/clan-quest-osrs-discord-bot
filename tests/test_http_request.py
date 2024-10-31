"""Test hiscores functionality."""

import pytest

from growlery.config import RUNESCAPE_HISCORES_LITE_URL, AccountType
from growlery.http_request import fetch_page_content


@pytest.mark.asyncio
async def test_fetch_page_content_default_status():
    """Test fetching page content with defalt status messages."""
    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode='',
            player_name='Ironman-Dia',
        ),
    )


@pytest.mark.asyncio
async def test_fetch_page_content_ironman_default_status():
    """Test fetching page content with defalt status messages."""
    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=AccountType.IRONMAN,
            player_name='Ironman-Dia',
        ),
    )


@pytest.mark.asyncio
async def test_fetch_page_content_ultimate_ironman_default_status():
    """Test fetching page content with defalt status messages."""
    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=AccountType.ULTIMATE_IRONMAN,
            player_name='Ironman-Dia',
        ),
    )


@pytest.mark.asyncio
async def test_fetch_page_content_hardcore_default_status():
    """Test fetching page content with defalt status messages."""
    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=AccountType.HARDCORE_IRONMAN,
            player_name='HCIMPrinessi',
        ),
    )


@pytest.mark.asyncio
async def test_fetch_page_content_1def_default_status():
    """Test fetching page content with defalt status messages."""
    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=AccountType.DEFENCE_PURE,
            player_name='HCIMPrinessi',
        ),
    )


@pytest.mark.asyncio
async def test_fetch_page_content_skiller_default_status():
    """Test fetching page content with defalt status messages."""
    assert await fetch_page_content(
        url=RUNESCAPE_HISCORES_LITE_URL.format(
            hiscores='_oldschool',
            gamemode=AccountType.SKILLER,
            player_name='Lvl-3',
        ),
    )


@pytest.mark.asyncio
async def test_fetch_page_content_bad_url():
    """Test error handling."""
    assert not await fetch_page_content(url="http://totallybrokenurlthisshouldnotwork.com")


@pytest.mark.asyncio
async def test_fetch_page_content_non_ok_status():
    """Test fetching page content and handing a non-OK status."""
    assert not await fetch_page_content(url="https://httpstat.us/404")
