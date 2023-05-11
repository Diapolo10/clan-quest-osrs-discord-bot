
# Growlery Changelog

All notable changes to this project will be documented in this file.

The format is based on [CHANGELOG.md][CHANGELOG.md]
and this project adheres to [Semantic Versioning][Semantic Versioning].

<!-- 
TEMPLATE

## [major.minor.patch] - yyyy-mm-dd

A message that notes the main changes in the update.

### Added

### Changed

### Deprecated

### Fixed

### Removed

### Security

_______________________________________________________________________________
 
 -->

<!--
EXAMPLE

## [0.2.0] - 2021-06-02

Lorem Ipsum dolor sit amet.

### Added

- Cat pictures hidden in the library
- Added beeswax to the gears

### Changed

- Updated localisation files

-->

<!--
_______________________________________________________________________________

## [0.3.0] - 2023-05-11

`README.md` is now more up-to-date, the new Wilderness bosses are now in the
list of bosses, and the project's linters were replaced with Ruff. The codebase
has also been cleaned up somewhat as a result in order to pass the new linter
guidelines.

### Added

- Added support for listing the new Wilderness bosses, fixing incorrect scores
  for existing bosses.

### Changed

- Updated `README.md` with clearer instructions for using the bot
- Updated dependencies
- Updated localisation files

### Fixed

- Boss hiscores are no longer broken

-->

_______________________________________________________________________________

## [0.3.0] - 2023-05-11

`README.md` is now more up-to-date, the new Wilderness bosses are now in the
list of bosses, and the project's linters were replaced with Ruff. The codebase
has also been cleaned up somewhat as a result in order to pass the new linter
guidelines.

### Added

- Added support for listing the new Wilderness bosses, fixing incorrect scores
  for existing bosses.

### Changed

- Updated `README.md` with clearer instructions for using the bot
- Updated dependencies
- Updated localisation files

### Fixed

- Boss hiscores are no longer broken

_______________________________________________________________________________

## [0.2.2] - 2023-03-09

Added better instructions to `README.md`, and enhanced tests.

### Added

- Tests for HTTP requests

### Changed

- Updated `README.md` with clearer instructions for using the bot
- Updated dependencies
- Improved test coverage
- Updated localisation files

_______________________________________________________________________________

## [0.2.1] - 2023-03-01

Small fixes to `README.md` and project matadata.

### Added

- `py.typed`-file to announce the package uses type hints

### Changed

- Updated localisation files

### Fixed

- PyPI badges in `README.md` now work correctly, and some broken badges were
  removed
- Corrected the list of supported Python versions

_______________________________________________________________________________

## [0.2.0] - 2023-03-01

Adds logging, full hiscores support (excluding RSN saving for Discord IDs),
plenty of workflow updates, removed vulnerable dependencies, added unit tests,
and updated `README.md`.

### Added

- Logging to files
- Support for fetching the following data from hiscores for all supported game
  modes, except Group Ironman:
  - Skill levels
  - Minigame hiscores
  - Boss kills
- Unit tests for hiscores
- Preliminary support for launching the program as a module

### Changed

- Updated `README.md`
- Updated localisation files

### Removed

- Removed `py` as an indirect dependency by upgrading the minimum Python
  version to accommodate for Tox no longer needing it
- Removed `pyproject-flake8` as a dependency, replacing it with
  `flake8-pyproject`, to make the dependencies more robust to changes.

_______________________________________________________________________________

## [0.1.0] - 2023-02-18

This is the initial version of the project. No official release has been
published as there's basically no functionality.

### Added

- The base project

[CHANGELOG.md]: https://web.archive.org/web/20220330064336/https://changelog.md/
[Semantic Versioning]: http://semver.org/

<!-- markdownlint-configure-file {
    "MD022": false,
    "MD024": false,
    "MD030": false,
    "MD032": false
} -->
<!--
    MD022: Blanks around headings
    MD024: No duplicate headings
    MD030: Spaces after list markers
    MD032: Blanks around lists
-->
