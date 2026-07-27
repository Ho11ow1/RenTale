init 999 python in rentale:
    def ShowDevScreen():
        if renpy.config.developer:
            renpy.show_screen("RenTale_DevScreen")

    renpy.config.start_callbacks.append(ShowDevScreen)
    renpy.config.after_load_callbacks.append(ShowDevScreen)
