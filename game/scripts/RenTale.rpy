# Namespace setup
init -10 python:
    from types import SimpleNamespace

    RenTale = SimpleNamespace()
    RenTale.Managers = SimpleNamespace()
    RenTale.ExtendedCharacter = ExtendedCharacter
    RenTale.Flags = None


# Managers
init -9 python:
    RenTale.Managers.FlagManager = FlagManager
    RenTale.Managers.SceneManager = SceneManager
    RenTale.Managers.GalleryManager = GalleryManager
    RenTale.Managers.TimeManager = None


# Instantiate instance based classes for renpy.store to be able to pickle them
default renTaleFlags = Flags()
default timeManager = TimeManager()


# Store hooks
init -1 python:
    galleryCache = {}

    def RestoreRenTaleInstances():
        import store
        if hasattr(store, "renTaleFlags"):
            RenTale.Flags = store.renTaleFlags
        if hasattr(store, "timeManager"):
            RenTale.Managers.TimeManager = store.timeManager


    def DeSerializeGallery():
        for name, data in persistent.gallery.items():
            galleryCache[name] = GalleryItem.FromDict(data)
    

    config.start_callbacks.append(RestoreRenTaleInstances)
    config.start_callbacks.append(DeSerializeGallery)

