# Qtile driver rice

This is my Qtile daily driver rice.

## Installing

To use it, first clone the repository to your dotfiles folder

**Clone somewhere you would like to keep it**

```sh
git clone https://github.com/Sniper10754/dotfiles
```

change directory to the dotfiles directory just cloned
```
cd dotfiles
```

*** Moving the dotfiles dir or the `qtile-driver-rice` dir will invalidate your qtile configuration.

use GNU `stow` or another link farm manager to create the required symlinks:

```sh
stow qtile-driver-rice
```

## Changes required to make it work
**Required**: 
- **Change the launcher** in `commands.py`, in my config i use a custom crafted one in rust (Ill soon publish it)
- **Change the font name** in `appearance.py`, in my config i used `Iosevka Nerd Font`

**Optional**:
- Install the pip package `dbus-next`

- Install the pip package `iwlib` for the wifi icon 

- Install `brightnessctl` for the brightness switches on your keyboard and the backlight widget on the qtile bar

- Install `libpulse` library (*Installed by default if you have pulse audio*) and the pip package `pulsectl_asyncio` both for adjusting the volume using the volume switches or the widget (scrolling on it)

- Change the compositor in `commands.py` or install the default one, `picom` (Check out my picom config!)

- *On X11*, If dragging/resizing a window is laggy change the `X11_DRAG_POLLING_RATE` to your display (in case you have more than 1 display the highest refresh rate between all of your displays) refresh rate.
