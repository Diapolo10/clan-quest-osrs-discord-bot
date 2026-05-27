"""Clan Quest OSRS hiscore bot."""

import importlib

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"
