"""Tests hiscores functionality"""

import discord.ext.test as dpytest
import pytest

from growlery.config import (
    COMMAND_PREFIX,
)

TEST_USERNAMES_HARDCORE = (
    'HCIMPrinessi',
    'xfrazx',
)
TEST_USERNAMES_ULTIMATE = (
    'Ironman-Dia',
)
TEST_USERNAMES_GIM = (
    'Ferrous Fran',
    'GrIM Verac',
)
TEST_USERNAMES_IRONMAN = ('Francine Fe', *TEST_USERNAMES_HARDCORE, *TEST_USERNAMES_ULTIMATE)
TEST_USERNAMES_SKILLER = (
    'Lvl-3',
)
TEST_USERNAMES_1DEF_PURE = (
    '1DefNoBank',
)
TEST_USERS_REGULAR = (
    'Choto 3000',
    'Francine1225',
    'iiDefend',
    'LazyKernel',
    'Santa Ends',
    'Sk8r Dan Man',
    'bendzo',  # High EHB and boss kill count
)
TEST_USERS = (
    TEST_USERS_REGULAR
    + TEST_USERNAMES_GIM
    + TEST_USERNAMES_IRONMAN
    + TEST_USERNAMES_SKILLER
    + TEST_USERNAMES_1DEF_PURE
)
NONEXISTENT_USER = "Idonotexistandneverwill"


@pytest.mark.asyncio()
async def test_no_name_given(bot):  # pylint: disable=W0613
    """Tests commands without name input"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs")
    assert dpytest.verify().message().content("Username assigning to Discord profile not implemented yet.")

    await dpytest.message(f"{COMMAND_PREFIX}07hs-minigames")
    assert dpytest.verify().message().content("Username assigning to Discord profile not implemented yet.")

    await dpytest.message(f"{COMMAND_PREFIX}07hs-bosses")
    assert dpytest.verify().message().content("Username assigning to Discord profile not implemented yet.")


@pytest.mark.asyncio()
async def test_normal_success(bot):  # pylint: disable=W0613
    """Tests posting the stats of a regular account"""

    for user in TEST_USERS:
        await dpytest.message(f"{COMMAND_PREFIX}07hs {user}")
        assert dpytest.verify().message().contains().content(f"STATS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_normal_failure(bot):  # pylint: disable=W0613
    """Tests posting the stats of a nonexistent regular account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_ironman_success(bot):  # pylint: disable=W0613
    """Tests posting the stats of an ironman account"""

    for user in TEST_USERNAMES_IRONMAN:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-im {user}")
        assert dpytest.verify().message().contains().content(f"STATS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_ironman_failure(bot):  # pylint: disable=W0613
    """Tests posting the stats of a nonexistent ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-im {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_hardcore_ironman_success(bot):  # pylint: disable=W0613
    """Tests posting the stats of a hardcore ironman account"""

    for user in TEST_USERNAMES_HARDCORE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim {user}")
        assert dpytest.verify().message().contains().content(f"STATS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_hardcore_ironman_failure(bot):  # pylint: disable=W0613
    """Tests posting the stats of a nonexistent hardcore ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_ultimate_ironman_success(bot):  # pylint: disable=W0613
    """Tests posting the stats of an ultimate ironman account"""

    for user in TEST_USERNAMES_ULTIMATE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-uim {user}")
        assert dpytest.verify().message().contains().content(f"STATS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_ultimate_ironman_failure(bot):  # pylint: disable=W0613
    """Tests posting the stats of a nonexistent ultimate ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_skiller_success(bot):  # pylint: disable=W0613
    """Tests posting the stats of a skiller account"""

    for user in TEST_USERNAMES_SKILLER:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller {user}")
        assert dpytest.verify().message().contains().content(f"STATS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_skiller_failure(bot):  # pylint: disable=W0613
    """Tests posting the stats of a nonexistent skiller account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_1def_pure_success(bot):  # pylint: disable=W0613
    """Tests posting the stats of a 1-Defence pure account"""

    for user in TEST_USERNAMES_1DEF_PURE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-def {user}")
        assert dpytest.verify().message().contains().content(f"STATS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_1def_pure_failure(bot):  # pylint: disable=W0613
    """Tests posting the stats of a nonexistent 1-Defence pure account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-def {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_normal_minigames_success(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a regular account"""

    for user in TEST_USERS:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-minigames {user}")
        assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_normal_minigames_failure(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a nonexistent regular account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-minigames {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_ironman_minigames_success(bot):  # pylint: disable=W0613
    """Tests posting the minigames of an ironman account"""

    for user in TEST_USERNAMES_IRONMAN:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-im-minigames {user}")
        assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_ironman_minigames_failure(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a nonexistent ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-im-minigames {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_hardcore_ironman_minigames_success(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a hardcore ironman account"""

    for user in TEST_USERNAMES_HARDCORE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-minigames {user}")
        assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_hardcore_ironman_minigames_failure(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a nonexistent hardcore ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-minigames {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_ultimate_ironman_minigames_success(bot):  # pylint: disable=W0613
    """Tests posting the minigames of an ultimate ironman account"""

    for user in TEST_USERNAMES_ULTIMATE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-minigames {user}")
        assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_ultimate_ironman_minigames_failure(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a nonexistent ultimate ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-minigames {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_skiller_minigames_success(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a skiller account"""

    for user in TEST_USERNAMES_SKILLER:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-minigames {user}")
        assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_skiller_minigames_failure(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a nonexistent skiller account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-minigames {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_1def_pure_minigames_success(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a 1-Defence pure account"""

    for user in TEST_USERNAMES_1DEF_PURE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-def-minigames {user}")
        assert dpytest.verify().message().contains().content(f"MINIGAMES FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_1def_pure_minigames_failure(bot):  # pylint: disable=W0613
    """Tests posting the minigames of a nonexistent 1-Defence pure account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-def-minigames {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_normal_bosses_success(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a regular account"""

    for user in TEST_USERS:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-bosses {user}")
        assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_normal_bosses_failure(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a nonexistent regular account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-bosses {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_ironman_bosses_success(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of an ironman account"""

    for user in TEST_USERNAMES_IRONMAN:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-im-bosses {user}")
        assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_ironman_bosses_failure(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a nonexistent ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-im-bosses {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_hardcore_ironman_bosses_success(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a hardcore ironman account"""

    for user in TEST_USERNAMES_HARDCORE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-bosses {user}")
        assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_hardcore_ironman_bosses_failure(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a nonexistent hardcore ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-hcim-bosses {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_ultimate_ironman_bosses_success(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of an ultimate ironman account"""

    for user in TEST_USERNAMES_ULTIMATE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-bosses {user}")
        assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_ultimate_ironman_bosses_failure(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a nonexistent ultimate ironman account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-uim-bosses {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_skiller_bosses_success(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a skiller account"""

    for user in TEST_USERNAMES_SKILLER:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-bosses {user}")
        assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_skiller_bosses_failure(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a nonexistent skiller account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-skiller-bosses {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")


@pytest.mark.asyncio()
async def test_1def_pure_bosses_success(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a 1-Defence pure account"""

    for user in TEST_USERNAMES_1DEF_PURE:
        await dpytest.message(f"{COMMAND_PREFIX}07hs-def-bosses {user}")
        assert dpytest.verify().message().contains().content(f"BOSS KILLS FOR {user.upper()}")


@pytest.mark.asyncio()
async def test_1def_pure_bosses_failure(bot):  # pylint: disable=W0613
    """Tests posting the boss kills of a nonexistent 1-Defence pure account"""

    await dpytest.message(f"{COMMAND_PREFIX}07hs-def-bosses {NONEXISTENT_USER}")
    assert dpytest.verify().message().content("Hiscores not found.")
