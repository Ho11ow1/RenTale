screen preferences():
    tag menu

    use game_menu(_("")):
        vbox:
            style "custom_pref_vbox"

            hbox:
                xsize 500
                spacing 20

                label _("Display"):
                    yoffset 5
                    text_style "custom_pref_label_text"

                imagebutton:
                    idle "gui/RenTale/UI/Separator.png"
                    sensitive False

                hbox:
                    spacing 20

                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            hbox:
                if persistent.has_autosave:
                    label _("Autosaves (Enabled)"):
                        style "custom_pref_label"
                    imagebutton:
                        idle "gui/RenTale/UI/Square-Checked.png"
                        hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                        action [SetVariable("config.has_autosave", False), SetVariable("persistent.has_autosave", False)]
                else:
                    label _("Autosaves (Disabled)"):
                        style "custom_pref_label"
                    imagebutton:
                        idle "gui/RenTale/UI/Square.png"
                        hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                        action [SetVariable("config.has_autosave", True), SetVariable("persistent.has_autosave", True)]

            hbox:
                if persistent.has_quicksave:
                    label _("Quicksaves (Enabled)"):
                        style "custom_pref_label"
                    imagebutton:
                        idle "gui/RenTale/UI/Square-Checked.png"
                        hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                        action [SetVariable("config.has_quicksave", False), SetVariable("persistent.has_quicksave", False)]
                else:
                    label _("Quicksaves (Disabled)"):
                        style "custom_pref_label"
                    imagebutton:
                        idle "gui/RenTale/UI/Square.png"
                        hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                        action [SetVariable("config.has_quicksave", True), SetVariable("persistent.has_quicksave", True)]

            hbox:
                if persistent.quickmenu_enabled:
                    label _("Quickmenu (Enabled)"):
                        style "custom_pref_label"
                    imagebutton:
                        idle "gui/RenTale/UI/Square-Checked.png"
                        hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                        action [SetVariable("quick_menu", False), SetVariable("persistent.quickmenu_enabled", False)]
                else:
                    label _("Quickmenu (Disabled)"):
                        style "custom_pref_label"
                    imagebutton:
                        idle "gui/RenTale/UI/Square.png"
                        hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                        action [SetVariable("quick_menu", True), SetVariable("persistent.quickmenu_enabled", True)]

            hbox:
                xsize 500
                spacing 20

                label _("Quickmenu position"):
                    yoffset 5
                    text_style "custom_pref_label_text"
                imagebutton:
                    idle "gui/RenTale/UI/Separator.png"
                    sensitive False

                hbox:
                    spacing 20

                    if persistent.quickmenu_position_x == 0.0:
                        textbutton "Left" action [SetVariable("persistent.quickmenu_position_x", 0.0)] xoffset -5
                    else:
                        textbutton "Left" action [SetVariable("persistent.quickmenu_position_x", 0.0)] xoffset -5
                    if persistent.quickmenu_position_x == 0.5:
                        textbutton "Center" action [SetVariable("persistent.quickmenu_position_x", 0.5)] xoffset -5
                    else:
                        textbutton "Center" action [SetVariable("persistent.quickmenu_position_x", 0.5)] xoffset -5
                    if persistent.quickmenu_position_x == 1.0:
                        textbutton "Right" action [SetVariable("persistent.quickmenu_position_x", 1.0)] xoffset -5
                    else:
                        textbutton "Right" action [SetVariable("persistent.quickmenu_position_x", 1.0)] xoffset -5

            hbox:
                spacing 20

                label _("Quickmenu items"):
                    yoffset 5
                    text_style "custom_pref_label_text"
                imagebutton:
                    idle "gui/RenTale/UI/Separator.png"
                    sensitive False

                hbox:
                    spacing 20

                    if persistent.quickmenu_rollback_enabled:
                        textbutton "Back" action [SetVariable("persistent.quickmenu_rollback_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Back" action [SetVariable("persistent.quickmenu_rollback_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_history_enabled:
                        textbutton "History" action [SetVariable("persistent.quickmenu_history_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "History" action [SetVariable("persistent.quickmenu_history_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_skip_enabled:
                        textbutton "Skip" action [SetVariable("persistent.quickmenu_skip_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Skip" action [SetVariable("persistent.quickmenu_skip_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_autosave_enabled:
                        textbutton "Auto" action [SetVariable("persistent.quickmenu_autosave_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Auto" action [SetVariable("persistent.quickmenu_autosave_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_save_enabled:
                        textbutton "Save" action [SetVariable("persistent.quickmenu_save_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Save" action [SetVariable("persistent.quickmenu_save_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_quicksave_enabled:
                        textbutton "Q.Save" action [SetVariable("persistent.quickmenu_quicksave_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Q.Save" action [SetVariable("persistent.quickmenu_quicksave_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_quickload_enabled:
                        textbutton "Q.Load" action [SetVariable("persistent.quickmenu_quickload_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Q.Load" action [SetVariable("persistent.quickmenu_quickload_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"
                    if persistent.quickmenu_prefs_enabled:
                        textbutton "Prefs" action [SetVariable("persistent.quickmenu_prefs_enabled", False)]:
                            text_style "custom_pref_quickmenu_enabled"
                    else:
                        textbutton "Prefs" action [SetVariable("persistent.quickmenu_prefs_enabled", True)]:
                            text_style "custom_pref_quickmenu_disabled"


screen Audio_Preferences():
    tag menu

    use game_menu(_("")):
        vbox:
            style "custom_pref_vbox"

            hbox:
                label _("Volume Master"):
                    style "custom_pref_label"
                bar value Preference("main volume"):
                    style "custom_pref_slider"

            if config.has_music:
                hbox:
                    label _("Volume BGM"):
                        style "custom_pref_label"
                    bar value Preference("music volume"):
                        style "custom_pref_slider"

            if config.has_sound:
                hbox:
                    label _("Volume SFX"):
                        style "custom_pref_label"
                    bar value Preference("sound volume"):
                        style "custom_pref_slider"

            if config.has_voice:
                hbox:
                    label _("Volume VO"):
                        style "custom_pref_label"
                    bar value Preference("voice volume"):
                        style "custom_pref_slider"

            hbox:
                label _("Mute All"):
                    style "custom_pref_label"
                imagebutton:
                    idle "gui/RenTale/UI/Square.png"
                    selected_idle "gui/RenTale/UI/Square-Checked.png"
                    selected_hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                    hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                    action Preference("all mute", "toggle")

screen Dialogue_Preferences():
    tag menu

    use game_menu(_("")):
        vbox:
            style "custom_pref_vbox"

            hbox:
                xsize 500
                spacing 20

                label _("Rollback Side"):
                    yoffset 5
                    text_style "custom_pref_label_text"
                imagebutton:
                    idle "gui/RenTale/UI/Separator.png"
                    sensitive False

                hbox:
                    spacing 20

                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

            hbox:
                label _("Text Speed"):
                    style "custom_pref_label"
                bar value Preference("text speed"):
                    style "custom_pref_slider"

            hbox:
                label _("Auto-Forward Time"):
                    style "custom_pref_label"
                bar value Preference("auto-forward time"):
                    style "custom_pref_slider"

            hbox:
                label _("Skip Unseen Text"):
                    style "custom_pref_label"
                imagebutton:
                    idle "gui/RenTale/UI/Square.png"
                    selected_idle "gui/RenTale/UI/Square-Checked.png"
                    selected_hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                    hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                    action Preference("skip", "toggle")

            hbox:
                label _("Skip After Choices"):
                    style "custom_pref_label"
                imagebutton:
                    idle "gui/RenTale/UI/Square.png"
                    selected_idle "gui/RenTale/UI/Square-Checked.png"
                    selected_hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                    hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                    action Preference("after choices", "toggle")

            hbox:
                label _("Skip Transitions"):
                    style "custom_pref_label"
                imagebutton:
                    idle "gui/RenTale/UI/Square.png"
                    selected_idle "gui/RenTale/UI/Square-Checked.png"
                    selected_hover Transform("gui/RenTale/UI/Square-Checked.png", matrixcolor = TintMatrix(gui.hover_color))
                    hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix(gui.hover_color))
                    action InvertSelected(Preference("transitions", "toggle"))

            hbox:
                label _("Text box opacity"):
                    style "custom_pref_label"
                bar value FieldValue(persistent, "textbox_opacity", range = 1.0, style = "slider"):
                    style "custom_pref_slider"

            hbox:
                label _("Text box height"):
                    style "custom_pref_label"
                bar value FieldValue(persistent, "textbox_height", offset = 225, range = 125, style = "slider"):
                    style "custom_pref_slider"

            hbox:
                style "custom_pref_hbox"
                label _("Text box width"):
                    style "custom_pref_label"
                bar value FieldValue(persistent, "textbox_width", offset = 1000, range = 646, style = "slider"):
                    style "custom_pref_slider"


style radio_label is pref_label
style radio_label_text is pref_label_text
style check_label is pref_label
style check_label_text is pref_label_text
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style check_button_text is gui_button_text
style radio_button_text is gui_button_text
style slider_button_text is gui_button_text

style custom_pref_label:
    xsize 460
    yoffset -15

style custom_pref_label_text:
    color gui.interface_text_color

style custom_pref_slider:
    xsize 400

style custom_pref_vbox:
    align (0.5, 0.5)
    offset (70, 20)
    spacing 40

style custom_pref_hbox:
    yalign 0.5

style custom_pref_quickmenu_enabled:
    font gui.interface_text_font
    color gui.accent_color
    hover_color gui.hover_color
    yoffset 5
    size 23

style custom_pref_quickmenu_disabled:
    font gui.interface_text_font
    color gui.idle_color
    hover_color gui.hover_color
    yoffset 5
    size 23

style custom_menu_btn:
    font gui.interface_text_font
    color gui.interface_text_color
    insensitive_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.accent_color

style pref_label is gui_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text is gui_label_text:
    yalign 1.0

style pref_vbox is vbox:
    xsize 338

style radio_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style radio_button is gui_button:
    background Frame((["gui/phone/button/radio_[prefix_]background.png", "gui/phone/button/[prefix_]background.png"] if renpy.variant("small") else []) + ["gui/button/radio_[prefix_]background.png", "gui/button/[prefix_]background.png"], gui.radio_button_borders, tile = gui.button_tile)
    padding gui.radio_button_borders.padding
    foreground "gui/button/radio_[prefix_]foreground.png"

style check_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style check_button is gui_button:
    background Frame((["gui/phone/button/check_[prefix_]background.png", "gui/phone/button/[prefix_]background.png"] if renpy.variant("small") else []) + ["gui/button/check_[prefix_]background.png", "gui/button/[prefix_]background.png"], gui.check_button_borders, tile = gui.button_tile)
    padding gui.check_button_borders.padding
    foreground "gui/button/check_[prefix_]foreground.png"

style slider_slider is gui_slider:
    xsize 525

style slider_button is gui_button:
    background Frame((["gui/phone/button/slider_[prefix_]background.png", "gui/phone/button/[prefix_]background.png"] if renpy.variant("small") else []) + ["gui/button/slider_[prefix_]background.png", "gui/button/[prefix_]background.png"], gui.button_borders, tile = gui.button_tile)
    yalign 0.5
    left_margin 15

style slider_vbox:
    xsize 675
