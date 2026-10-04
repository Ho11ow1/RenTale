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
    properties gui.button_properties("choice_button")


style choice_button_text is button_text:
    properties gui.text_properties("choice_button")
