screen main_menu():
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background

    vbox:
        align (0.0, 0.0)
        offset (30, 20)
        spacing 20

        showif url_patreon is not None:
            imagebutton:
                idle "images/logos/normal/patreon.png"
                hover Transform("images/logos/normal/patreon.png", matrixcolor = BrightnessMatrix(0.1))
                hover_sound (url_hover_sound if url_hover_sound is not None else None)
                action OpenURL(url_patreon)

        showif url_discord is not None:
            imagebutton:
                idle "images/logos/normal/discord.png"
                hover Transform("images/logos/normal/discord.png", matrixcolor = BrightnessMatrix(0.1))
                hover_sound (url_hover_sound if url_hover_sound is not None else None)
                action OpenURL(url_discord)


    hbox:
        align (0.5, 0.98)
        spacing 75

        textbutton _("NEW GAME") action Start() text_style "custom_menu_btn"
        textbutton _("CONTINUE") action ShowMenu("load") text_style "custom_menu_btn"
        textbutton _("OPTIONS") action ShowMenu("preferences") text_style "custom_menu_btn"
        textbutton _("GALLERY") action ShowMenu("Gallery") text_style "custom_menu_btn"
        textbutton _("QUIT") action Quit(True) text_style "custom_menu_btn"
        text "VERSION [config.version]" yalign 0.5 color gui.text_color


style main_menu_version is main_menu_text

style main_menu_frame is empty:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"

style main_menu_text is gui_text:
    color gui.accent_color
    xalign gui.main_menu_text_xalign
    textalign gui.main_menu_text_xalign

style main_menu_title is main_menu_text:
    size gui.title_text_size
