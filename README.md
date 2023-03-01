# Growlery - The Clan Quest OSRS Discord Bot

![Stuff](./docs/assets/cq_logo_wide.png)

Ever since the untimely demise of RuneInfo, there's been a lack of OSRS support in the Discord bot department. While RuneScape 3 has Elenora, it doesn't support OSRS.

The Council of Elders looked about them and saw regression, not progress. The decision was made by the wisest: a new bot would be hardened and removed from the cycle. Its power would herald a new era.

| Type         | Badges |
|--------------|---|
| PyPI         | ![Python versions](https://img.shields.io/pypi/pyversions/growlery?logo=python) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/growlery) ![Wheel](https://img.shields.io/pypi/wheel/growlery?logo=pypi) ![Downloads](https://img.shields.io/pypi/dm/growlery?logo=pypi) [![Version](https://img.shields.io/pypi/v/growlery)](https://pypi.org/project/growlery/) |
| Tests        | [![codecov](https://codecov.io/gh/Diapolo10/clan-quest-osrs-discord-bot/branch/main/graph/badge.svg?token=N3JOBzERqP)](https://codecov.io/gh/Diapolo10/clan-quest-osrs-discord-bot) ![Unit tests](https://github.com/diapolo10/clan-quest-osrs-discord-bot/workflows/Unit%20tests/badge.svg) ![Pylint](https://github.com/diapolo10/clan-quest-osrs-discord-bot/workflows/Pylint/badge.svg) ![Flake8](https://github.com/diapolo10/clan-quest-osrs-discord-bot/workflows/Flake8/badge.svg) ![Deploy to PyPI](https://github.com/diapolo10/clan-quest-osrs-discord-bot/workflows/Deploy%20to%20PyPI/badge.svg) |
| Activity     | ![GitHub contributors](https://img.shields.io/github/contributors/diapolo10/clan-quest-osrs-discord-bot) ![Last commit](https://img.shields.io/github/last-commit/diapolo10/clan-quest-osrs-discord-bot?logo=github) ![GitHub all releases](https://img.shields.io/github/downloads/diapolo10/clan-quest-osrs-discord-bot/total?logo=github) ![GitHub issues](https://img.shields.io/github/issues/diapolo10/clan-quest-osrs-discord-bot) ![GitHub closed issues](https://img.shields.io/github/issues-closed/diapolo10/clan-quest-osrs-discord-bot) ![GitHub pull requests](https://img.shields.io/github/issues-pr/diapolo10/clan-quest-osrs-discord-bot) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/diapolo10/clan-quest-osrs-discord-bot) |
| QA           | [![CodeFactor](https://www.codefactor.io/repository/github/diapolo10/clan-quest-osrs-discord-bot/badge?logo=codefactor)](https://www.codefactor.io/repository/github/diapolo10/clan-quest-osrs-discord-bot) [![Rating](https://img.shields.io/librariesio/sourcerank/pypi/growlery)](https://libraries.io/github/Diapolo10/clan-quest-osrs-discord-bot/sourcerank) |
| Other        | [![License](https://img.shields.io/github/license/diapolo10/clan-quest-osrs-discord-bot)](https://opensource.org/licenses/MIT) ![Repository size](https://img.shields.io/github/repo-size/diapolo10/clan-quest-osrs-discord-bot?logo=github) ![Code size](https://img.shields.io/github/languages/code-size/diapolo10/clan-quest-osrs-discord-bot?logo=github) ![Lines of code](https://img.shields.io/tokei/lines/github/diapolo10/clan-quest-osrs-discord-bot?logo=github) |

## Installation

The project is currently only available as source code, but full releases should eventually be available via PyPI

```sh
pip install growlery
```

and as GitHub releases.

Installation requires Python 3.10 or newer. Platform-independent.

To run the bot, either manually execute `growlery/main.py` or, for future releases, you can attempt to run it via

```sh
python -m growlery
```

in case the functionality has been implemented.

## Features

- Minimal dependencies
- Supports fetching and printing hiscores, minigame scores, and boss kills as formatted text tables on Discord
- Graceful handling of invalid usernames

## Caught a Bug?

1. [Fork][Forking a repository] this repository to your own GitHub account and then [clone][Cloning a repository] it to your local device
2. Install `poetry` (if it isn't already installed)
3. Run `poetry install` in the project directory. This fetches development dependencies like `pytest` and sets up everything for you to start debugging

As always, you can run the tests using: `poetry run pytest`

[Forking a repository]: https://help.github.com/articles/fork-a-repo/
[Cloning a repository]: https://help.github.com/articles/cloning-a-repository/

<!-- markdownlint-configure-file {
    "MD022": false,
    "MD024": false,
    "MD030": false,
    "MD032": false,
    "MD033": false
} -->
<!--
    MD022: Blanks around headings
    MD024: No duplicate headings
    MD030: Spaces after list markers
    MD032: Blanks around lists
    MD033: No inline HTML
-->
