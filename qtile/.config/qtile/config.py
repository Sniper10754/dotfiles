from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

import subprocess

import os
from pathlib import Path
import importlib

DOTFILES_DIR = Path.joinpath(
    Path(os.getcwd()), 
    ".config",
    "qtile"
)

# Import the colors.py file assuming the dotfiles directory is `$HOME/.config/qtile`
import sys

# Import colors from current directory
spec = importlib.util.spec_from_file_location("colors", Path.joinpath(
    DOTFILES_DIR, 
    "colors.py"
))

colors_mod = importlib.util.module_from_spec(spec)

sys.modules["colors"] = colors_mod

spec.loader.exec_module(colors_mod)

import colors

# Done

GAPS = 4

WALLPAPER_PATH = Path.joinpath(DOTFILES_DIR, "wallpaper-gruvbox.png")

FONT = "Iosevka Nerd Font"
FONT_SIZE = 15

LEFT = "left"
RIGHT = "right"
DOWN = "down"
UP = "up"

TERMINAL = guess_terminal(preference = "kitty")
LAUNCHER = "ulauncher"
COMPOSITOR = ["picom"]
MOD = "mod4"

# Compatibility 
mod = MOD

@hook.subscribe.startup
def _():
    subprocess.Popen(COMPOSITOR)

    ...

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([MOD], LEFT, lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], RIGHT, lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], DOWN, lazy.layout.down(), desc="Move focus down"),
    Key([MOD], UP, lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD, "shift"], LEFT, lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([MOD, "shift"], RIGHT, lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([MOD, "shift"], DOWN, lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], UP, lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Key([mod, "space"], lazy.layout.floating_enable(), desc="Set window to floating mode"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [MOD],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([MOD], "space", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD], "r", lazy.spawn(LAUNCHER), desc="Run the launcher"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Tile(
        border_width=GAPS,
        border_focus=colors.background,
        border_normal=colors.background,
    ),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=GAPS),
    layout.Max(),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=FONT,
    fontsize=FONT_SIZE,
    padding=8,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper=WALLPAPER_PATH,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background = colors.purple
                ),
                widget.GroupBox(
                    active = colors.yellow,
                    highlight_method = "line"
                ),

                widget.Spacer(),
                widget.WindowName(),
                widget.Spacer(),

                widget.Spacer(
                    length = 16
                ),
                
                widget.Battery(
                    format = "{percent:2.0%}",
                    update_interval = 10,
                    
                    background = colors.green, 
                ),
                widget.StatusNotifier(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p")
            ],
            size = 24,
            background = colors.background,
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
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
