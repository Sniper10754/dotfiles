from libqtile.utils import guess_terminal
from pathlib import Path

import homedir_constants

# Audio

MUTE_PULSEAUDIO_CMD = ["pactl", "set-sink-volume", "0", "-100%"]

AUDIO_STEP = 5

RAISE_PULSEAUDIO_VOLUME = ["pactl", "set-sink-volume", "0", f"+{AUDIO_STEP}%"]
LOWER_PULSEAUDIO_VOLUME = ["pactl", "set-sink-volume", "0", f"-{AUDIO_STEP}%"]

# Video

BRIGHTNESS_STEP = 10

INCREASE_BRIGHTNESS_CMD = ["brightnessctl", "set", f"+{BRIGHTNESS_STEP}%"]
DECREASE_BRIGHTNESS_CMD = ["brightnessctl", "set", f"{BRIGHTNESS_STEP}%-"]

# Programs

TERMINAL_CMD = [guess_terminal(preference="kitty")]
LAUNCHER_CMD = [
    str(Path.joinpath(homedir_constants.USER_HOME, ".cargo/bin/frozen-launcher"))
]

COMPOSITOR_CMD = ["picom"]
