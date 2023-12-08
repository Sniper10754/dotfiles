from libqtile import widget
from qtile_extras import widget as extra_widget

from pathlib import Path

import appearance

backlight_name = next(Path("/sys/class/backlight").iterdir())

PRIMARY_SCREEN_WIDGETS = [
    widget.CurrentLayout(background=appearance.purple),
    widget.GroupBox(active=appearance.yellow, highlight_method="line"),
    widget.Spacer(),
    widget.WindowName(),
    widget.Spacer(),
    extra_widget.Systray(),
    widget.PulseVolume(format="", background=appearance.yellow),
    widget.Battery(
        format="BAT: {percent:2.0%}",
        update_interval=10,
        background=appearance.green,
    ),
    widget.Backlight(
        background=appearance.gray,
        change_command="brightnessctl s {0}",
        step=3,
        backlight_name=backlight_name,
    ),
    widget.Clock(
        format="%Y-%m-%d %a %I:%M %p",
    ),
]
