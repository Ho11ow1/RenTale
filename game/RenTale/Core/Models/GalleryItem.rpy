init -100 python: 
    class GalleryItem():
        def __init__(self, label, isUnlocked = False):
            if type(label) != str:
                raise TypeError(f"")
            if type(isUnlocked) != bool:
                raise TypeError(f"")

            self.Label = label
            self.IsUnlocked = isUnlocked

        