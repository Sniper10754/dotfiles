from libqtile.config import Screen
from libqtile import bar, widget

import appearance

PRIMARY_SCREEN = Screen(
    wallpaper=appearance.WALLPAPER_PATH,
    wallpaper_mode="fill",
    top=bar.Bar(
        [
            widget.CurrentLayout(
                background=appearance.purple
            ),
            widget.GroupBox(
                active=appearance.yellow,
                highlight_method="line"
            ),

            widget.Spacer(),
            widget.WindowName(),
            widget.Spacer(),

            widget.Battery(
                format="{percent:2.0%}",
                update_interval=10,

                background=appearance.green,
            ),
            widget.StatusNotifier(),
            widget.Clock(format="%Y-%m-%d %a %I:%M %p")
        ],
        size=24,
        background=appearance.background,
    ),
    right=bar.Gap(5),
    left=bar.Gap(5),
    bottom=bar.Gap(5),
    # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
    # By default we handle these events delayed to already improve performance, however your system might still be struggling
    # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
    x11_drag_polling_rate=60,
)

SECONDARY_SCREEN = Screen(
    wallpaper=appearance.WALLPAPER_PATH,
    wallpaper_mode="fill",
    top=bar.Bar(
        [
            widget.Spacer(),

            widget.Clock(format="%Y-%m-%d %a %I:%M %p")
        ],
        size=24,
        background=appearance.background,
    ),
    right=bar.Gap(5),
    left=bar.Gap(5),
    bottom=bar.Gap(5),
    # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
    # By default we handle these events delayed to already improve performance, however your system might still be struggling
    # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
    x11_drag_polling_rate=60,
)

