init 1 python:
    from store import _window_hide

    class SceneManager:
        """
            A simple utility for common Ren'Py actions with the addition of hiding the dialogue box
        """

        def CleanJump(labelName, trans = False, auto = False):
            """
                Hides the dialogue window and jumps to a specified label.

                Args:
                    labelName (string): The name of the label to jump to.
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.

                Raises:
                    TypeError: If labelName is not a string instance.
            """

            if type(labelName) != str:
                raise TypeError(f"Expected string, got {type(labelName).__name__}")

            _window_hide(trans, auto)
            renpy.jump(labelName)


        def CleanCall(labelName, fromCurrent = False, trans = False, auto = False):
            """
                Hides the dialogue window and calls the specified label.

                Args:
                    labelName (string): The name of the label to jump to.
                    fromCurrent (bool): On return come back to this statement or next.
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.

                Raises:
                    TypeError: If labelName is not a string instance.
            """

            if type(labelName) != str:
                raise TypeError(f"Expected string, got {type(labelName).__name__}")

            _window_hide(trans, auto)
            renpy.call(labelName, fromCurrent)


        def CleanCallScreen(screenName, trans = False, auto = False):
            """
                Hides the dialogue window and calls the specified window.

                Args:
                    screenName (string): The name of the label to jump to.
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.

                Returns:
                    Screen: Returns the screen Return() action just like [ call screen "screenName"].

                Raises:
                    TypeError: If labelName is not a string instance.
            """

            if type(screenName) != str:
                raise TypeError(f"Expected string, got {type(screenName).__name__}")

            _window_hide(trans, auto)
            return renpy.call_screen(screenName)


        def HideWindow(trans = False, auto = False):
            """
                Hides the dialogue window and jumps to a specified label.

                Args:
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.
            """

            _window_hide(trans, auto)

