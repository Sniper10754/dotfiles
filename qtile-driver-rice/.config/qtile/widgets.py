from pathlib import Path

from libqtile import widget
from qtile_extras import widget as extra_widget

import appearance

try:
    backlight_name = next(Path("/sys/class/backlight").iterdir()).name
except StopIteration:
    backlight_name = None

try:
    wifi_interface = next(
        filter(
            lambda path: "wlp" in path.name or "wlan" in path.name,
            Path("/sys/class/net/").iterdir(),
        )
    ).name
except StopIteration:
    wifi_interface = None

try:
    battery_name = next(
        filter(
            lambda power_supply: "BAT" in power_supply.name,
            Path("/sys/class/power_supply").iterdir(),
        )
    ).name
except StopIteration:
    battery_name = None

NULL_SPACER = widget.Spacer(0)

CURRENT_LAYOUT_WIDGET = widget.CurrentLayout(
    background=appearance.purple
)

PULSEAUDIO_WIDGET = widget.PulseVolume(
    fmt="VOLUME: {}", 
    background=appearance.yellow
)

WIFI_ICON = extra_widget.WiFiIcon(
    background=appearance.blue,
    active_colour=appearance.foreground,
    disconnected_colour=appearance.background,
    interface=wifi_interface,
) if wifi_interface != None else NULL_SPACER

BATTERY_WIDGET = widget.Battery(
    format="BAT: {percent:2.0%}",
    update_interval=10,
    background=appearance.green,
    low_background=appearance.red,
) if battery_name != None else NULL_SPACER

BACKLIGHT_WIDGET = widget.Backlight(
    background=appearance.gray,
    fmt="BACKLIGHT: {}",
    step=3,
    change_command="brightnessctl s {0}%",
    backlight_name=backlight_name,
) if backlight_name != None else NULL_SPACER

CLOCK_WIDGET = widget.Clock(
    format="%d-%m-%Y %I:%M",
)

SEP = widget.Sep(
    foreground=appearance.foreground,
    padding=7,
    linewidth=2,
    size_percent=100
)

PRIMARY_SCREEN_WIDGETS = [
    CURRENT_LAYOUT_WIDGET,
    widget.GroupBox(
        block_highlight_text_color=appearance.yellow,

        highlight_method='block'
    ),
    widget.Spacer(),
    widget.WindowName(),
    widget.Spacer(),
    extra_widget.Systray(),
    SEP,
    PULSEAUDIO_WIDGET,
    WIFI_ICON,
    BATTERY_WIDGET,
    BACKLIGHT_WIDGET,
    SEP,
    CLOCK_WIDGET,
]

SECONDARY_SCREEN_WIDGETS = [
    widget.Spacer(),
    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
]
