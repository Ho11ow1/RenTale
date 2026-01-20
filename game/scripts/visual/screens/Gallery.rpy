screen Gallery():
    tag menu

    use game_menu(_("Gallery"), scroll = "viewport"):
        style_prefix "Gallery"

        grid 3 4:
            spacing 10

            for name, data in persistent.gallery.items():
                vbox:
                    if data["IsUnlocked"]:
                        imagebutton:
                            action Replay(data["Scene"], scope = {}, locked = False)
                            idle data["Thumbnail"]
                            xysize (200, 150)
                    else:
                        imagebutton:
                            action NullAction()
                            idle Transform(data["Thumbnail"], matrixcolor = SaturationMatrix(0))
                            xysize (200, 150)
                    
