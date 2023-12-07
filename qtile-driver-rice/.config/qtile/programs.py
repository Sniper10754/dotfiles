from libqtile.utils import guess_terminal
from pathlib import Path

import homedir_constants

TERMINAL_CMD = guess_terminal(preference="kitty")
LAUNCHER_CMD = str(Path.joinpath(
    homedir_constants.USER_HOME, ".cargo/bin/frozen-launcher"))
COMPOSITOR_CMD = ["picom"]
