from libqtile import widget
from qtile_extras import widget as extra_widget

from pathlib import Path

import appearance

try:
    backlight_name = next(Path("/sys/class/backlight").iterdir())
except StopIteration:
    backlight_name = None

try:
    wifi_interface = next(
        filter(
            lambda path: "wlp" in path.name or "wlan" in path.name,
            Path("/sys/class/net/").iterdir(),
        )
    )
except StopIteration:
    wifi_interface = None

try:
    battery_name = next(
        filter(
            lambda power_supply: "BAT" in power_supply.name,
            Path("/sys/class/power_supply").iterdir(),
        )
    )
except StopIteration:
    battery_name = None

PRIMARY_SCREEN_WIDGETS = [
    widget.CurrentLayout(background=appearance.purple),
    widget.GroupBox(active=appearance.yellow, highlight_method="line"),
    widget.Spacer(),
    widget.WindowName(),
    widget.Spacer(),
    extra_widget.Systray(),
    widget.PulseVolume(fmt="VOLUME: {}", background=appearance.yellow),
    extra_widget.WiFiIcon(
        background=appearance.blue,
        active_colour=appearance.foreground,
        disconnected_colour=appearance.background,
        interface=wifi_interface.name or "wlp2s0",
    ),
    widget.Battery(
        format="BAT: {percent:2.0%}",
        update_interval=10,
        background=appearance.green,
        low_background=appearance.red,
    ) if battery_name != None else widget.Spacer(0),
    widget.Backlight(
        background=appearance.gray,
        fmt="BACKLIGHT: {}",
        step=3,
        change_command="brightnessctl s {0}%",
        backlight_name=backlight_name,
    ) if backlight_name != None else widget.Spacer(0),
    widget.Clock(
        format="%Y-%m-%d %a %I:%M %p",
    ),
]

SECONDARY_SCREEN_WIDGETS = [
    widget.Spacer(),
    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
]
