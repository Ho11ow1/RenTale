screen Audio_Settings():
    tag menu
    style_prefix "pref"

    use game_menu(_("")):

        vpgrid:
            cols 2
            rows 5

            # Kind of cheating with the hbox but it works and there's no need to do any magic styles so be it
            hbox:
                label _("Volume Master")
            bar value Preference("main volume")
            
            hbox:            
                label _("Volume BGM")
            bar value Preference("music volume")
            
            hbox:
                label _("Volume SFX")
            bar value Preference("sound volume")
            
            hbox:
                label _("Volume VO")
            bar value Preference("voice volume")
            
            hbox:            
                label _("Mute All")
            imagebutton:
                idle "gui/RenTale/UI/Square.png"
                selected_idle Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#FF0000"))
                hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#ff85ab"))
                action Preference("all mute", "toggle")
