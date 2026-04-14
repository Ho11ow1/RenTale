screen Gallery():
    tag menu

    use game_menu(_("Gallery"), scroll = "viewport"):

        frame:
            style "empty"

            has vpgrid
            cols 4
            spacing 75

            textbutton "Willow" action Show("GalleryPage", filteredList = RenTale_Generate_Filtered_List("Willow"))
            textbutton "Alice" action Show("GalleryPage", filteredList = RenTale_Generate_Filtered_List("Alice"))


screen GalleryPage(filteredList):
    tag menu

    use game_menu(_("Gallery"), scroll = "viewport"):

        frame:
            style "empty"

            has vpgrid
            cols 4
            spacing 75

            for item in filteredList:
                imagebutton:
                    padding (0, 0)
                    xysize (360, 200)

                    if item.IsUnlocked:
                        idle item.Thumbnail
                        hover Transform(item.Thumbnail, matrixcolor = BrightnessMatrix(0.1))
                        action Replay(item.Label, item.Scope, False)
                        sensitive True
                    else:
                        idle "images/Gallery/Locked.png"
                        hover "images/Gallery/Locked.png"
                        sensitive False
