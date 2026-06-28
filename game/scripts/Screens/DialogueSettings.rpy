screen Dialogue_Settings():
    tag menu
    style_prefix "pref"
    
    use game_menu(_("")):

        vpgrid:
            cols 2
            rows 6

            hbox:
                label _("Rollback Side")
                imagebutton:
                    idle "gui/RenTale/UI/Separator.png"
                    sensitive False

            hbox:
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            label _("Text Speed")
            bar value Preference("text speed")

            label _("Auto-Forward Time")
            bar value Preference("auto-forward time")


            label _("Skip Unseen Text")
            imagebutton:
                idle "gui/RenTale/UI/Square.png"
                selected_idle Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#FF0000"))
                hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#ff85ab"))
                action Preference("skip", "toggle")

            label _("Skip After Choices")
            imagebutton:
                idle "gui/RenTale/UI/Square.png"
                selected_idle Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#FF0000"))
                hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#ff85ab"))
                action Preference("after choices", "toggle")

            label _("Skip Transitions")
            imagebutton:
                idle "gui/RenTale/UI/Square.png"
                selected_idle Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#FF0000"))
                hover Transform("gui/RenTale/UI/Square.png", matrixcolor = TintMatrix("#ff85ab"))
                action InvertSelected(Preference("transitions", "toggle"))
