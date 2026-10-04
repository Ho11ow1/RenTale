init python:
    config.character_id_prefixes.append("namebox")


screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        ypos 1080 - (persistent.textbox_height) - (32 if persistent.quickmenu_enabled else 0)
        xsize persistent.textbox_width + 274
        ysize persistent.textbox_height
        background Frame(Transform("gui/textbox.png", alpha = persistent.textbox_opacity))

        vbox:
            xpos gui.name_xpos
            ypos 20
            xsize persistent.textbox_width
            spacing 10

            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


screen multiple_say(who, what, multiple):
    style_prefix "say"

    window:
        id "window"
        ypos 1080 - (persistent.textbox_height * multiple[0]) - (32 if persistent.quickmenu_enabled else 0)
        xsize persistent.textbox_width + 274
        ysize persistent.textbox_height
        background Frame(Transform("gui/textbox.png", alpha = persistent.textbox_opacity))

        vbox:
            xpos gui.name_xpos
            ypos 20
            xsize persistent.textbox_width
            spacing 10

            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style say_thought is say_dialogue
style namebox_label is say_label


style window is default:
    xalign 0.5


style block2_multiple2_say_window:
    yalign -0.1


style namebox is default:
    xsize gui.namebox_width
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding


style say_label is default:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5


style say_dialogue is default:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
