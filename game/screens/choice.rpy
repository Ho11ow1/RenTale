screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is button:
    background Frame((["gui/phone/button/choice_[prefix_]background.png", "gui/phone/button/[prefix_]background.png"] if renpy.variant("small") else []) + ["gui/button/choice_[prefix_]background.png", "gui/button/[prefix_]background.png"], gui.choice_button_borders, tile = gui.choice_button_tile)
    padding gui.choice_button_borders.padding
    xysize (gui.choice_button_width, gui.choice_button_height)

style choice_button_text is button_text:
    font gui.choice_button_text_font
    size gui.choice_button_text_size
    xalign gui.choice_button_text_xalign
    textalign gui.choice_button_text_xalign
    layout "subtitle"
    idle_color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color
