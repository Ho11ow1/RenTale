init -100 python in rentale:
    class GalleryItem():
        def __init__(self, name: str, label: str, image: str, scope: dict | None = None, is_unlocked: bool = False):
            """
            Represents a gallery scene. Automatically registers into rentale.gallery_list and persistent.rentale_gallery on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(label) != str:
                raise RenTaleTypeError(str, type(label))
            if type(image) != str:
                raise RenTaleTypeError(str, type(image))
            if scope is not None and type(scope) != dict:
                raise RenTaleTypeError((dict, type(None)), type(scope))
            if type(is_unlocked) != bool:
                raise RenTaleTypeError(bool, type(is_unlocked))

            self.name = name
            self.label = label
            self.image = image
            self.scope = {} if scope is None else scope

            if name not in renpy.store.persistent.rentale_gallery:
                renpy.store.persistent.rentale_gallery[name] = is_unlocked
                self.is_unlocked = is_unlocked
            else:
                self.is_unlocked = renpy.store.persistent.rentale_gallery[name]

            gallery_list.add(self)

        
        def unlock(self) -> None:
            """
            Sets the 'is_unlocked' variable to true and unlocks itself in the gallery if not already unlocked
            """
            if not self.is_unlocked:
                self.is_unlocked = True
                renpy.store.persistent.rentale_gallery[self.name] = True
