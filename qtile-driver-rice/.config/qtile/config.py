from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

import subprocess

import homedir_constants
import screens as cfg_screens
import keybinds
import appearance
import programs


@hook.subscribe.startup
def _():
    subprocess.Popen(programs.COMPOSITOR_CMD)

    ...


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([keybinds.MOD], keybinds.LEFT_KEY,
        lazy.layout.left(), desc="Move focus to left"),
    Key([keybinds.MOD], keybinds.RIGHT_KEY,
        lazy.layout.right(), desc="Move focus to right"),
    Key([keybinds.MOD], keybinds.DOWN_KEY,
        lazy.layout.down(), desc="Move focus down"),
    Key([keybinds.MOD], keybinds.UP_KEY, lazy.layout.up(), desc="Move focus up"),
    Key([keybinds.MOD], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([keybinds.MOD, "shift"], keybinds.LEFT_KEY, lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([keybinds.MOD, "shift"], keybinds.RIGHT_KEY, lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([keybinds.MOD, "shift"], keybinds.DOWN_KEY,
        lazy.layout.shuffle_down(), desc="Move window down"),
    Key([keybinds.MOD, "shift"], keybinds.UP_KEY,
        lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([keybinds.MOD, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([keybinds.MOD, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([keybinds.MOD, "control"], "j",
        lazy.layout.grow_down(), desc="Grow window down"),
    Key([keybinds.MOD, "control"], "k",
        lazy.layout.grow_up(), desc="Grow window up"),
    Key([keybinds.MOD], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    # Key([keys.MOD, "space"], lazy.layout.floating_enable(), desc="Set window to floating keys.MODe"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [keybinds.MOD, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([keybinds.MOD], "Return", lazy.spawn(
        programs.TERMINAL_CMD), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([keybinds.MOD], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([keybinds.MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [keybinds.MOD],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([keybinds.MOD], "space", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([keybinds.MOD, "control"], "r",
        lazy.reload_config(), desc="Reload the config"),
    Key([keybinds.MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([keybinds.MOD], "r", lazy.spawn(
        programs.LAUNCHER_CMD), desc="Run the launcher"),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer -c 0 sset Master 1+ unmute"))
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # keys.MOD1 + letter of group = switch to group
            Key(
                [keybinds.MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # keys.MOD1 + shift + letter of group = switch to & move focused window to group
            Key(
                [keybinds.MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # keys.MOD1 + shift + letter of group = move focused window to group
            # Key([keys.MOD, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Tile(
        border_width=appearance.WIN_BORDER_WIDTH,
        border_focus=appearance.background,
        border_normal=appearance.background,
        margin=5
    ),
    layout.Columns(border_focus_stack=[
                   "#d75f5f", "#8f3d3d"], border_width=appearance.WIN_BORDER_WIDTH),
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
mouse = [
    Drag([keybinds.MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([keybinds.MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([keybinds.MOD], "Button2", lazy.window.bring_to_front()),
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
