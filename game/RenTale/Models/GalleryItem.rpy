init -100 python in rentale:
    class GalleryItem():
        def __init__(self, name, label, thumbnail, scope = None, isUnlocked = False):
            """
            Represents a gallery scene. Automatically registers into rentale.gallery_list and persistent.rentale_gallery on creation.
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

            if name not in renpy.store.persistent.rentale_gallery:
                renpy.store.persistent.rentale_gallery[name] = isUnlocked
                self.IsUnlocked = isUnlocked
            else:
                self.IsUnlocked = renpy.store.persistent.rentale_gallery[name]

            gallery_list.add(self)

        
        def unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true and unlocks itself in the gallery if not already unlocked
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True
                renpy.store.persistent.rentale_gallery[self.Name] = True
