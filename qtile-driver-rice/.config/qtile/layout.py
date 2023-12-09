from libqtile import layout
from libqtile.config import Match

import appearance

layouts = [
    layout.Columns(
        border_focus_stack=[appearance.purple, appearance.gray],
        border_width=appearance.WIN_BORDER_WIDTH,
        margin=appearance.GAPS,
    ),
    layout.Tile(
        border_width=appearance.WIN_BORDER_WIDTH,
        border_focus=appearance.WIN_BORDER_COLOR_FOCUSED,
        border_normal=appearance.WIN_BORDER_COLOR_NORMAL,
        margin=appearance.GAPS,
    ),
    layout.Floating(),

    # Try more layouts by unleashing below layouts.
    # layout.Max(),
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
