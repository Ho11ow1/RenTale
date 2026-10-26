init offset = -1

style prompt_text is gui_text

style default:
    font gui.text_font
    size gui.text_size
    language gui.language

style input:
    adjust_spacing False
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_underline True

style gui_text:
    color gui.interface_text_color
    size gui.interface_text_size
    font gui.interface_text_font

style button:
    xysize (gui.button_width, gui.button_height)
    padding (0, 0, 0, 5)

style button_text is gui_text:
    font gui.button_text_font
    size gui.button_text_size
    align (gui.button_text_xalign, 0.5)
    idle_color gui.button_text_idle_color
    hover_color gui.button_text_hover_color
    selected_color gui.button_text_selected_color
    insensitive_color gui.button_text_insensitive_color

style label_text is gui_text:
    size gui.text_size
    color gui.accent_color

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile = gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile = gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile = gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile = gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile = gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile = gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile = gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile = gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile = gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile = gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile = gui.frame_tile)
