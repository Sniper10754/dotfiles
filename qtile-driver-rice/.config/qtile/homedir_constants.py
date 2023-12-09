from pathlib import Path

import os

USER_HOME = Path(os.getcwd())

CONFIG_DIR = Path.joinpath(USER_HOME, ".config", "qtile")
