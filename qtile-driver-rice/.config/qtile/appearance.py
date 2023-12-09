from pathlib import Path

import homedir_constants


# Gruvbox Dark mode
# https://github.com/morhetz/gruvbox

# Change as you wish

background = "#282828"
foreground = "#ebdbb2"

gray = "#928374"
red = "#fb46934"
green = "#b8bb26"
yellow = "#fabd2f"
blue = "#83a598"
purple = "#d3869b"
aqua = "#8ec07c"


# Window manager properties

GAPS = 5
WIN_BORDER_WIDTH = 2
WIN_BORDER_COLOR_NORMAL = background
WIN_BORDER_COLOR_FOCUSED = gray

FONT = "Iosevka Nerd Font"
FONT_SIZE = 15

WALLPAPER_PATH = Path.joinpath(homedir_constants.CONFIG_DIR, "wallpaper-gruvbox.png")

# Widget defaults
widget_defaults = {
    "font": FONT,
    "fontsize": FONT_SIZE,
    "padding": 8,
}

extension_defaults = widget_defaults.copy()
