screen navigation():

    hbox:
        align (0.5, 0.08)
        spacing 30

        textbutton _("SAVE") action ShowMenu("save") text_style "custom_menu_btn"
        imagebutton:
            idle "gui/RenTale/UI/Separator.png"
            sensitive False

        textbutton _("LOAD") action ShowMenu("load") text_style "custom_menu_btn"
        imagebutton:
            idle "gui/RenTale/UI/Separator.png"
            sensitive False

        textbutton _("AUDIO") action ShowMenu("Audio_Preferences") text_style "custom_menu_btn"
        imagebutton:
            idle "gui/RenTale/UI/Separator.png"
            sensitive False

        textbutton _("DIALOGUE") action ShowMenu("Dialogue_Preferences") text_style "custom_menu_btn"
        imagebutton:
            idle "gui/RenTale/UI/Separator.png"
            sensitive False

        textbutton _("SETTINGS") action ShowMenu("preferences") text_style "custom_menu_btn"

        if _in_replay:
            imagebutton:
                idle "gui/RenTale/UI/Separator.png"
                sensitive False

            textbutton _("END REPLAY") action EndReplay(confirm = True) text_style "custom_menu_btn"


style navigation_button is gui_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")


style navigation_button_text is gui_button_text:
    properties gui.text_properties("navigation_button")
