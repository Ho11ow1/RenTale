screen game_menu(title, scroll = None, yinitial = 0.0, spacing = 0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    hbox:
        align (0.0, 0.0)
        spacing 20

        textbutton _("MAIN MENU") action MainMenu() text_style "custom_menu_btn"
        textbutton _("QUIT") action Quit(True) text_style "custom_menu_btn"

    hbox:
        align (0.0, 1.0)

        textbutton _("RETURN") action Return() text_style "custom_menu_btn"

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_scrollbar is gui_vscrollbar
style return_button_text is navigation_button_text

style game_menu_outer_frame is empty:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame is empty:
    xsize 420
    yfill True

style game_menu_content_frame is empty:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport is gui_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side is gui_side:
    spacing 15

style game_menu_label is gui_label:
    xpos 75
    ysize 180

style game_menu_label_text is gui_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button is navigation_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
