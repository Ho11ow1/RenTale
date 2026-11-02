transform notify_appear:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0

    on hide:
        linear 0.5 alpha 0.0


transform delayed_blink(delay, cycle):
    alpha 0.5

    pause delay

    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat


screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide("notify")


style notify_frame is empty
style notify_text is gui_text

style skip_frame is empty:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile = gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text is gui_text:
    size gui.notify_text_size

style skip_triangle is skip_text:
    font "DejaVuSans.ttf"

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile = gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size
