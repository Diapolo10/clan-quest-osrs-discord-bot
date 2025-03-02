"""Test hiscores functionality."""


import discord.ext.test as dpytest
import pytest
from discord.ext.commands.bot import Bot
from pytest_mock import MockerFixture

from growlery.config import (
    COMMAND_PREFIX,
)

BOSS_USER = "bendzo"
HCIM_USER = "HCIMPrinessi"
NONEXISTENT_USER = "Idonotexistandneverwill"
SKILLER_USER = "Lvl3 Coach"
UIM_1DEF_USER = "1DefNoBank"


@pytest.mark.asyncio
async def test_no_name_given(bot: Bot):
    """Test commands without name input."""
    await dpytest.message(f"{COMMAND_PREFIX}07hs")
    assert dpytest.verify().message().content("Username assigning to Discord profile not implemented yet.")

    await dpytest.message(f"{COMMAND_PREFIX}07hs-minigames")
    assert dpytest.verify().message().content("Username assigning to Discord profile not implemented yet.")

    await dpytest.message(f"{COMMAND_PREFIX}07hs-bosses")
    assert dpytest.verify().message().content("Username assigning to Discord profile not implemented yet.")


@pytest.mark.asyncio
async def test_normal_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the stats of a regular account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"STATS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_normal_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the stats of a nonexistent regular account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_ironman_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the stats of an ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-im {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"STATS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_ironman_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the stats of a nonexistent ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-im {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_hardcore_ironman_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the stats of a hardcore ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim {HCIM_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"STATS FOR {HCIM_USER.upper()}"), message


@pytest.mark.asyncio
async def test_hardcore_ironman_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the stats of a nonexistent hardcore ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_ultimate_ironman_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the stats of an ultimate ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"STATS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_ultimate_ironman_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the stats of a nonexistent ultimate ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_skiller_success(bot: Bot, mocker: MockerFixture, mock_skiller_data: str):
    """Test posting the stats of a skiller account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_skiller_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller {SKILLER_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"STATS FOR {SKILLER_USER.upper()}"), message


@pytest.mark.asyncio
async def test_skiller_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the stats of a nonexistent skiller account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_1def_pure_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the stats of a 1-Defence pure account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-def {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"STATS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_1def_pure_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the stats of a nonexistent 1-Defence pure account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-def {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_normal_minigames_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the minigames of a regular account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-minigames {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_normal_minigames_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the minigames of a nonexistent regular account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-minigames {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_ironman_minigames_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the minigames of an ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-im-minigames {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_ironman_minigames_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the minigames of a nonexistent ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-im-minigames {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_hardcore_ironman_minigames_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the minigames of a hardcore ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-minigames {HCIM_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {HCIM_USER.upper()}"), message


@pytest.mark.asyncio
async def test_hardcore_ironman_minigames_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the minigames of a nonexistent hardcore ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-minigames {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_ultimate_ironman_minigames_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the minigames of an ultimate ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-minigames {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_ultimate_ironman_minigames_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the minigames of a nonexistent ultimate ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-minigames {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_skiller_minigames_success(bot: Bot, mocker: MockerFixture, mock_skiller_data: str):
    """Test posting the minigames of a skiller account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_skiller_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-minigames {SKILLER_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {SKILLER_USER.upper()}"), message


@pytest.mark.asyncio
async def test_skiller_minigames_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the minigames of a nonexistent skiller account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-minigames {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_1def_pure_minigames_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the minigames of a 1-Defence pure account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-def-minigames {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_1def_pure_minigames_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the minigames of a nonexistent 1-Defence pure account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-def-minigames {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_normal_bosses_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the boss kills of a regular account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-bosses {BOSS_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {BOSS_USER.upper()}"), message


@pytest.mark.asyncio
async def test_normal_bosses_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the boss kills of a nonexistent regular account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-bosses {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_ironman_bosses_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the boss kills of an ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-im-bosses {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_ironman_bosses_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the boss kills of a nonexistent ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-im-bosses {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_hardcore_ironman_bosses_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the boss kills of a hardcore ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-bosses {HCIM_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {HCIM_USER.upper()}"), message


@pytest.mark.asyncio
async def test_hardcore_ironman_bosses_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the boss kills of a nonexistent hardcore ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-bosses {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_ultimate_ironman_bosses_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the boss kills of an ultimate ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-bosses {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_ultimate_ironman_bosses_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the boss kills of a nonexistent ultimate ironman account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-bosses {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_skiller_bosses_success(bot: Bot, mocker: MockerFixture, mock_skiller_data: str):
    """Test posting the boss kills of a skiller account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_skiller_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-bosses {SKILLER_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {SKILLER_USER.upper()}"), message


@pytest.mark.asyncio
async def test_skiller_bosses_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the boss kills of a nonexistent skiller account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-bosses {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message


@pytest.mark.asyncio
async def test_1def_pure_bosses_success(bot: Bot, mocker: MockerFixture, mock_user_data: str):
    """Test posting the boss kills of a 1-Defence pure account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value=mock_user_data)
    await dpytest.message(f"{COMMAND_PREFIX}07hs-def-bosses {UIM_1DEF_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {UIM_1DEF_USER.upper()}"), message


@pytest.mark.asyncio
async def test_1def_pure_bosses_failure(bot: Bot, mocker: MockerFixture):
    """Test posting the boss kills of a nonexistent 1-Defence pure account."""
    mocker.patch('growlery.cogs.hiscores.fetch_page_content', return_value="")
    await dpytest.message(f"{COMMAND_PREFIX}07hs-def-bosses {NONEXISTENT_USER}")
    message = dpytest.get_message(peek=True).content
    assert dpytest.verify().message().content("Hiscores not found."), message
