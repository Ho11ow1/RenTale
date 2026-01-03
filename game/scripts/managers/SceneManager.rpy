init 1 python:
    from store import _window_hide

    class SceneManager:
        """
            A simple utility for common Ren'Py actions with the addition of hiding the dialogue box
        """

        @staticmethod
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


        @staticmethod
        def CleanCall(labelName, *args, fromCurrent = False, trans = False, auto = False, **kwargs):
            """
                Hides the dialogue window and calls the specified label.

                Args:
                    labelName (string): The name of the label to jump to.
                    *args: Positional arguments to pass to the label.
                    fromCurrent (bool): On return come back to this statement or next.
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.
                    **kwargs: Keyword arguments to pass to the label.

                Raises:
                    TypeError: If labelName is not a string instance.
            """

            if type(labelName) != str:
                raise TypeError(f"Expected string, got {type(labelName).__name__}")

            _window_hide(trans, auto)
            renpy.call(labelName, *args, from_current = fromCurrent, **kwargs)


        @staticmethod
        def CleanCallScreen(screenName, *args, with_none = True, mode = "screen", trans = False, auto = False, **kwargs):
            """
                Hides the dialogue window and calls the specified window.

                Args:
                    screenName (string): The name of the label to jump to.
                    *args: Positional arguments to pass to the screen.
                    with_none (bool): Whether to show the screen with None transition.
                    mode (string): The mode to use when showing the screen.
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.
                    **kwargs: Keyword arguments to pass to the screen.

                Returns:
                    Screen: Returns the screen Return() action just like [ call screen "screenName"].

                Raises:
                    TypeError: If labelName is not a string instance.
            """

            if type(screenName) != str:
                raise TypeError(f"Expected string, got {type(screenName).__name__}")

            _window_hide(trans, auto)
            return renpy.call_screen(screenName, *args, _with_none = with_none, _mode = mode, **kwargs)


        @staticmethod
        def HideWindow(trans = False, auto = False):
            """
                Hides the dialogue window and jumps to a specified label.

                Args:
                    trans (bool | None | Transition): Specifies the transition to use, None for none, False for default.
                    auto (bool): Act as window auto hide.
            """

            _window_hide(trans, auto)

