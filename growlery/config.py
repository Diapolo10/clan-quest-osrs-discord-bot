"""This file contains the global configuration settings for the Discord bot"""

import os
from enum import Enum
from pathlib import Path

from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).parent
ROOT_DIR = PROJECT_DIR.parent
DOCS_DIR = ROOT_DIR / 'docs'
CODE_EXAMPLES = DOCS_DIR / 'example_code'
ENV_FILE = PROJECT_DIR / '.env'

# Loads environmental variables from an .env-file
load_dotenv()

LOG_CONFIG = ROOT_DIR / 'logging.conf'
LOG_FILES = ROOT_DIR / 'logs' / 'growlery.log'
PYPROJECT_TOML = ROOT_DIR / 'pyproject.toml'

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./server.db'
SQLALCHEMY_TEST_DATABASE_URL = 'sqlite+aiosqlite:///./tests/test.db'

COMMAND_PREFIX = '/'
AUTH_TOKEN: str = os.getenv('DISCORD_TOKEN', 'NONEXISTENT')

LOG_FILES.parent.mkdir(parents=True, exist_ok=True)


SKILL_NAMES = (
    'Total',
    'Attack',
    'Defence',
    'Strength',
    'Hitpoints',
    'Ranged',
    'Prayer',
    'Magic',
    'Cooking',
    'Woodcutting',
    'Fletching',
    'Fishing',
    'Firemaking',
    'Crafting',
    'Smithing',
    'Mining',
    'Herblore',
    'Agility',
    'Thieving',
    'Slayer',
    'Farming',
    'Runecraft',
    'Hunter',
    'Construction',
)

MINIGAME_NAMES = (
    'Unknown Minigame',
    'Bounty Hunter - Hunter',
    'Bounty Hunter - Rogue',
    'Clue Scrolls (all)',
    'Clue Scrolls (beginner)',
    'Clue Scrolls (easy)',
    'Clue Scrolls (medium)',
    'Clue Scrolls (hard)',
    'Clue Scrolls (elite)',
    'Clue Scrolls (master)',
    'LMS - Rank',
    'PvP Arena - Rank',
    'Soul Wars Zeal',
    'Rifts closed',
)

BOSS_NAMES = (
    'Abyssal Sire',
    'Alchemical Hydra',
    'Artio',
    'Barrows Chests',
    'Bryophyta',
    'Callisto',
    'Calvar\'ion',
    'Cerberus',
    'Chambers of Xeric',
    'Chambers of Xeric: Challenge Mode',
    'Chaos Elemental',
    'Chaos Fanatic',
    'Commander Zilyana',
    'Corporeal Beast',
    'Crazy Archaeologist',
    'Dagannoth Prime',
    'Dagannoth Rex',
    'Dagannoth Supreme',
    'Deranged Archaeologist',
    'General Graardor',
    'Giant Mole',
    'Grotesque Guardians',
    'Hespori',
    'Kalphite Queen',
    'King Black Dragon',
    'Kraken',
    'Kree\'Arra',
    'K\'ril Tsutsaroth',
    'Mimic',
    'Nex',
    'Nightmare',
    'Phosani\'s Nightmare',
    'Obor',
    'Phantom Muspah',
    'Sarachnis',
    'Scorpia',
    'Skotizo',
    'Spindel',
    'Tempoross',
    'The Gauntlet',
    'The Corrupted Gauntlet',
    'Theatre of Blood',
    'Theatre of Blood: Hard Mode',
    'Thermonuclear Smoke Devil',
    'Tombs of Amascut',
    'Tombs of Amascut: Expert Mode',
    'TzKal-Zuk',
    'TzTok-Jad',
    'Venenatis',
    'Vet\'ion',
    'Vorkath',
    'Wintertodt',
    'Zalcano',
    'Zulrah',
)

RUNESCAPE_HISCORES_LITE_URL = (
    'http://services.runescape.com/m=hiscore{hiscores}{gamemode}/index_lite.ws?player={player_name}'
)


class AccountType(str, Enum):
    """Specifies different supported account types"""

    NORMAL = ''
    IRONMAN = '_ironman'
    HARDCORE_IRONMAN = '_hardcore_ironman'
    ULTIMATE_IRONMAN = '_ultimate'
    SKILLER = '_skiller'
    DEFENCE_PURE = '_skiller_defence'


class AccountTypeName(str, Enum):
    """Specifies names for different supported account types"""

    NORMAL = ''
    IRONMAN = 'Ironman'
    HARDCORE_IRONMAN = 'Hardcore'
    ULTIMATE_IRONMAN = 'Ultimate'
    SKILLER = 'Skiller'
    DEFENCE_PURE = 'Defence Pure'
