init 999 python:
    def RenTale_ShowDevScreen():
        if config.developer:
            renpy.show_screen("RenTale_DevScreen")

    config.start_callbacks.append(RenTale_ShowDevScreen)
    config.after_load_callbacks.append(RenTale_ShowDevScreen)
