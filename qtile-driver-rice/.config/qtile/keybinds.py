from libqtile.config import Group, Key
from libqtile.lazy import lazy

import commands

LEFT_KEY = "left"
RIGHT_KEY = "right"
DOWN_KEY = "down"
UP_KEY = "up"

MOD = "mod4"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key(
        [MOD], LEFT_KEY, lazy.layout.left(), desc="Move focus to left"
    ),
    Key(
        [MOD],
        RIGHT_KEY,
        lazy.layout.right(),
        desc="Move focus to right",
    ),
    Key([MOD], DOWN_KEY, lazy.layout.down(), desc="Move focus down"),
    Key([MOD], UP_KEY, lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [MOD, "shift"],
        LEFT_KEY,
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [MOD, "shift"],
        RIGHT_KEY,
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [MOD, "shift"],
        DOWN_KEY,
        lazy.layout.shuffle_down(),
        desc="Move window down",
    ),
    Key(
        [MOD, "shift"],
        UP_KEY,
        lazy.layout.shuffle_up(),
        desc="Move window up",
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [MOD, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [MOD, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(
        [MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"
    ),
    Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Key([keys.MOD, "space"], lazy.layout.floating_enable(), desc="Set window to floating keys.MODe"),
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
    Key(
        [MOD],
        "Return",
        lazy.spawn(commands.TERMINAL_CMD),
        desc="Launch terminal",
    ),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [MOD],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [MOD],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [MOD], "r", lazy.spawn(commands.LAUNCHER_CMD), desc="Run the launcher"
    ),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(commands.RAISE_PULSEAUDIO_VOLUME)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(commands.LOWER_PULSEAUDIO_VOLUME)),
    Key([], "XF86AudioMute", lazy.spawn(commands.MUTE_PULSEAUDIO_CMD)),
    Key([], "XF86MonBrightnessUp", lazy.spawn(commands.INCREASE_BRIGHTNESS_CMD)),
    Key([], "XF86MonBrightnessDown", lazy.spawn(commands.DECREASE_BRIGHTNESS_CMD)),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # keys.MOD1 + letter of group = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # keys.MOD1 + shift + letter of group = switch to & move focused window to group
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # keys.MOD1 + shift + letter of group = move focused window to group
            # Key([keys.MOD, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
