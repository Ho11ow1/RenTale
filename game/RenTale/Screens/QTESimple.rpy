screen QTE_Simple(duration = 1.3, prompt = "CLICK ME"):
    """
    A simple quick time event which stores it's return value in the renpy global variable "_return"
    
    Returns true on interaction
    """
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
            spacing 30

            bar:
                value AnimatedValue(0, 100, duration, 100)
                range 100
                xsize 600
                ysize 50
                xalign 0.5
                left_bar "gui/RenTale/QTE/bar.png" 
                right_bar Solid("#00000000")

            textbutton prompt:
                action Return(True)
                xsize 450
                xalign 0.5
                text_xalign 0.5
