from libqtile.log_utils import logger
from libqtile.config import Screen
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile import hook

from qtile_extras import widget as extra_widget

from textwrap import dedent
from pathlib import Path

import widgets
import appearance

X11_DRAG_POLLING_RATE = 144

PRIMARY_SCREEN = Screen(
    wallpaper=str(appearance.WALLPAPER_PATH),
    wallpaper_mode="fill",
    top=bar.Bar(
        widgets.PRIMARY_SCREEN_WIDGETS,
        size=24,
        background=appearance.background,
    ),
    # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
    # By default we handle these events delayed to already improve performance, however your system might still be struggling
    # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
    x11_drag_polling_rate=X11_DRAG_POLLING_RATE,
)

SECONDARY_SCREEN = Screen(
    wallpaper=str(appearance.WALLPAPER_PATH),
    wallpaper_mode="fill",
    top=bar.Bar(
        widgets.SECONDARY_SCREEN_WIDGETS,
        size=24,
        background=appearance.background,
    ),
    # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
    # By default we handle these events delayed to already improve performance, however your system might still be struggling
    # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
    x11_drag_polling_rate=X11_DRAG_POLLING_RATE,
)

screens = [PRIMARY_SCREEN, SECONDARY_SCREEN]
