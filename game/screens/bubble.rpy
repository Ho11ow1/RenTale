define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left": {
        "window_background": Transform(bubble.frame, xzoom = 1, yzoom = 1),
        "window_bottom_padding": 27,
    },

    "bottom_right": {
        "window_background": Transform(bubble.frame, xzoom = -1, yzoom = 1),
        "window_bottom_padding": 27,
    },

    "top_left": {
        "window_background": Transform(bubble.frame, xzoom = 1, yzoom = -1),
        "window_top_padding": 27,
    },

    "top_right": {
        "window_background": Transform(bubble.frame, xzoom = -1, yzoom = -1),
        "window_top_padding": 27,
    },

    "thought": {
        "window_background": bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left": (0, 0, 0, 22),
    "bottom_right": (0, 0, 0, 22),
    "top_left": (0, 22, 0, 0),
    "top_right": (0, 22, 0, 0),
    "thought": (0, 0, 0, 0),
}


screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox is empty:
    xalign 0.5

style bubble_who is default:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what is default:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"
