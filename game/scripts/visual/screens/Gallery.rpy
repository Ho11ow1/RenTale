screen Gallery():
    tag menu

    use game_menu(_("Gallery"), scroll = "viewport"):
        style_prefix "Gallery"

        # NOTE: This is a basic gallery layout.
        # You can customize this screen to add:
        # - Character tabs/filters
        # - Pagination with arrows
        # - List view instead of grid
        # - Search functionality
        #
        # For a clean solution use styles/Gallery_.rpy to customise visuals.
        #
        # See the Ren'Py documentation for screen language examples.

        grid 4 4:
        
            for name, data in persistent.gallery.items():
                if data["IsUnlocked"]:
                    imagebutton:
                        action Replay(data["Scene"], scope = {}, locked = False)
                        idle data["Thumbnail"]
                else:
                    imagebutton:
                        action NullAction()
                        idle Transform(data["Thumbnail"], matrixcolor = SaturationMatrix(0))
                    
