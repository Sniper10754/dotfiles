from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from libqtile import hook

import subprocess

import screens as cfg_screens
from keybinds import mouse, keys, groups
import appearance
import commands
from layout import layouts, floating_layout


@hook.subscribe.startup
def _():
    subprocess.Popen(commands.COMPOSITOR_CMD)


widget_defaults = {
    "font": appearance.FONT,
    "fontsize": appearance.FONT_SIZE,
    "padding": 8,
}

extension_defaults = widget_defaults.copy()

screens = [cfg_screens.PRIMARY_SCREEN]

# for _ in range(1):
#     screens.append()

# Drag floating layouts.


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"