screen input(prompt):
    style_prefix "input"

    window:
        ypos 1080 - (persistent.textbox_height) - (32 if persistent.quickmenu_enabled else 0)
        xysize (persistent.textbox_width + 274, persistent.textbox_height)
        background Frame(Transform("gui/textbox.png", alpha = persistent.textbox_opacity))

        vbox:
            pos (gui.name_xpos, 20)
            xsize persistent.textbox_width
            spacing 50

            text prompt style "input_prompt"

            hbox:
                spacing 5

                text "> " color gui.text_color
                input id "input"


screen confirm(message, yes_action, no_action):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            align (0.5, 0.5)
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_prompt is gui_prompt

style input_prompt is default:
    xalign gui.dialogue_text_xalign

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

style confirm_frame is gui_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile = gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    align (0.5, 0.5)

style confirm_prompt_text is gui_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button is gui_medium_button:
    background Frame((["gui/phone/button/confirm_[prefix_]background.png", "gui/phone/button/[prefix_]background.png"] if renpy.variant("small") else []) + ["gui/button/confirm_[prefix_]background.png", "gui/button/[prefix_]background.png"], gui.button_borders, tile = gui.button_tile)

style confirm_button_text is gui_medium_button_text:
    xalign gui.confirm_button_text_xalign
    textalign gui.confirm_button_text_xalign
    layout "subtitle"
