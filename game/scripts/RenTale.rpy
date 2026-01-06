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
    RenTale.Managers.TimeManager = None


# Instantiate instance based classes for renpy.store to be able to pickle them
default renTaleFlags = Flags()
default timeManager = TimeManager()


# Store hook | runs after load to restore instances previously set to null
init python:
    def RestoreRenTaleInstances():
        import store
        if hasattr(store, "renTaleFlags"):
            RenTale.Flags = store.renTaleFlags
        if hasattr(store, "timeManager"):
            RenTale.Managers.TimeManager = store.timeManager
    
    config.start_callbacks.append(RestoreRenTaleInstances)

