default persistent.gallery = {}

init python:
    def InitGallery():
        """
            Initialize all gallery items.
            Only adds items that don't already exist in persistent.gallery.
            This preserves unlock progress across game sessions.
        """

        galleryItems = [
            GalleryItem("Temp", False, "images/", "", None)
        ]

        for galleryItem in galleryItems:
            if galleryItem.Name not in persistent.gallery:
                RenTale.Managers.GalleryManager.Add(galleryItem)


    InitGallery()

