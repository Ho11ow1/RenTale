init -90 python:
    class GalleryManager():
        @staticmethod
        def Unlock(name: str) -> None:

            if type(name) != str:
                raise TypeError(f"Expected string, got {type(name).__name__}")
            if name not in persistent.gallery:
                raise ValueError(f"GalleryItem by the name of '{name}' does not exist under persistent.gallery")

            store.persistent.gallery[name]["IsUnlocked"] = True
