init -100 python: 
    class GalleryItem():
        def __init__(self, name, label, thumbnail, scope = None, isUnlocked = False):
            """
            Represents a gallery scene. Automatically registers into RenTale_Gallery_List and persistent.RenTale_Gallery on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(label) != str:
                raise RenTaleTypeError(str, type(label))
            if type(thumbnail) != str:
                raise RenTaleTypeError(str, type(thumbnail))
            if scope is not None and type(scope) != dict:
                raise RenTaleTypeError((dict, type(None)), type(scope))
            if type(isUnlocked) != bool:
                raise RenTaleTypeError(bool, type(isUnlocked))

            self.Name = name
            self.Label = label
            self.Thumbnail = thumbnail
            self.Scope = {} if scope is None else scope

            if name not in persistent.RenTale_Gallery:
                persistent.RenTale_Gallery[name] = isUnlocked
                self.IsUnlocked = isUnlocked
            else:
                self.IsUnlocked = persistent.RenTale_Gallery[name]

            RenTale_Gallery_List.add(self)

        
        def Unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true and unlocks itself in the gallery if not already unlocked
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True
                persistent.RenTale_Gallery[self.Name] = True
