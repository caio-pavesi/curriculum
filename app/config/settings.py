"""Environment variables to the project."""

import os
from pathlib import Path

# Project directory.
APP_DIRECTORY = Path(__file__).resolve().parent.parent

# User directory.
USER_DIRECTORY = Path(os.path.expanduser("~"))
