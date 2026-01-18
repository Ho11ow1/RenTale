screen QTE_Simple(promptText, duration = 1.3):
    modal True
    timer duration action Return(False)

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)

    frame:
        xfill True
        yfill True
        background None

        vbox:
            align (0.5, 0.5)
            spacing 50

            bar:
                value AnimatedValue(0, 100, duration, 100)
                range 100
                xsize 600
                ysize 50
                xalign 0.5
                left_bar "images/screens/bar.png"
                right_bar Solid("#00000000")

            textbutton promptText:
                action Return(True)
                xsize 450
                xalign 0.5
                text_xalign 0.5
                background "#00000080"
                hover_background "#222222"
                text_color "#ffffff"
                text_hover_color "#ffffff"

