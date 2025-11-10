init 1 python:
    from store import _window_hide

    class SceneManager:
        def CleanJump(labelName, trans = False, auto = False):
            if type(labelName) != str:
                raise TypeError(f"Expected string, got {type(labelName).__name__}")

            _window_hide(trans, auto)
            renpy.jump(labelName)


        def CleanCall(labelName, fromCurrent = False, trans = False, auto = False):
            if type(labelName) != str:
                raise TypeError(f"Expected string, got {type(labelName).__name__}")

            _window_hide(trans, auto)
            renpy.call(labelName, fromCurrent)


        def CleanCallScreen(screen_name, trans = False, auto = False):
            if type(screen_name) != str:
                raise TypeError(f"Expected string, got {type(screen_name).__name__}")

            _window_hide(trans, auto)
            return renpy.call_screen(screen_name)


        def HideWindow(trans = False, auto = False):
            _window_hide(trans, auto)
