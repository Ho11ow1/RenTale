init -10 python:
    class GalleryManager:
        """
            Utility class to manage GalleryItems safely
        """

        @classmethod
        def Add(cls, galleryItem: GalleryItem) -> None:
            """
                Adds a new gallery item to persistent.gallery.

                Args:
                    galleryItem (GalleryItem): Entire GalleryItem object to be added.

                Raises:
                    TypeError: If galleryItem is not a GalleryItem instance
                    ValueError: If an item with this name already exists.
            """

            if type(galleryItem) != GalleryItem:
                raise TypeError(f"Expected GalleryItem, got {type(galleryItem).__name__}")
            if cls.Exists(galleryItem.Name):
                raise ValueError(f"GalleryItem '{galleryItem.Name}' already exists in persistent.gallery")

            galleryCache[galleryItem.Name] = galleryItem
            persistent.gallery[galleryItem.Name] = galleryItem.ToDict()

        
        @classmethod
        def Get(cls, name: str) -> GalleryItem:
            """
                Retrieves a gallery item by name.

                Args:
                    name (string): Unique identifier of the gallery item.

                Raises:
                    TypeError: If name is not a string instance
                    ValueError: If persistent.gallery does not have an item identified by the given name

                Returns:
                    GalleryItem: The entire object.
            """

            if type(name) != str:
                raise TypeError(f"Expected string, got {type(name).__name__}")
            if not cls.Exists(name):
                raise ValueError(f"Could not find GalleryItem identified by '{name}")

            return galleryCache[name]


        @staticmethod
        def Exists(name: str) -> bool:
            """
                Checks if a gallery item exists.

                Args:
                    name (string): Unique identifier to check.

                Raises:
                    TypeError: If name is not a string instance.

                Returns:
                    bool: True if item exists, False otherwise.
            """

            if type(name) != str:
                raise TypeError(f"Expected string, got {type(name).__name__}")

            return name in galleryCache


        @classmethod
        def Unlock(cls, name: str) -> None:
            """
                Unlocks the specified gallery item.

                Args:
                    name (string): Unique identifier of the gallery item to be unlocked.

                Raises:
                    ValueError: If name is not associated with any gallery item inside of the persistent object.
            """

            if type(name) != str:
                raise TypeError(f"Expected string, got {type(name).__name__}")
            if not cls.Exists(name):
                raise ValueError(f"GalleryItem by the name of '{name}' does not exist under persistent.gallery")

            galleryCache[name].IsUnlocked = True
            persistent.gallery[name]["IsUnlocked"] = True


        @classmethod
        def IsUnlocked(cls, name: str) -> bool:
            """
                Checks if the specified gallery item is unlocked.

                Args:
                    name (string): Unique identifier of the gallery item to be checked.

                Raises:
                    ValueError: If name is not associated with any gallery item inside of the persistent object.
            """

            if type(name) != str:
                raise TypeError(f"Expected string, got {type(name).__name__}")
            if not cls.Exists(name):
                raise ValueError(f"GalleryItem by the name of '{name}' does not exist under persistent.gallery")
            
            return galleryCache[name].IsUnlocked

