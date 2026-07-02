screen Gallery():
    tag menu

    use game_menu(_("")):

        vpgrid:
            cols 4
            spacing 75

            textbutton "Willow" action ShowMenu("GalleryPage", filteredList = rentale.generate_filtered_list(prefix = "Willow"))
            textbutton "Alice" action ShowMenu("GalleryPage", filteredList = rentale.generate_filtered_list(prefix = "Alice"))


screen GalleryPage(filteredList):
    tag menu

    use game_menu(_("")):

        textbutton "<":
            xalign 1.0
            yalign 0.0
            action ShowMenu("Gallery")

        vpgrid:
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
                        idle "images/RenTale/Gallery/Locked.png"
                        hover "images/RenTale/Gallery/Locked.png"
                        sensitive False
