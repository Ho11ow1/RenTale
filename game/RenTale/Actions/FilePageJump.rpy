init -10 python in rentale:
    class FilePageJump(renpy.store.Action):
        """
        Allows jumping multiple pages in the save & load screen
        """
        def __init__(self, max = None, wrap = False, auto = True, quick = True, count = 1):
            if max is not None and type(max) != int:
                raise RenTaleTypeError((int, type(None)), type(max))
            if type(wrap) != bool:
                raise RenTaleTypeError(bool, type(wrap))
            if type(auto) != bool:
                raise RenTaleTypeError(bool, type(auto))
            if type(quick) != bool:
                raise RenTaleTypeError(bool, type(quick))
            if type(count) != int:
                raise RenTaleTypeError(int, type(count))

            if count == 0:
                return

            autoEnabled = renpy.config.has_autosave and auto
            quickEnabled = renpy.config.has_quicksave and quick
            configOffset = (1 if autoEnabled else 0) + (1 if quickEnabled else 0)

            page = renpy.store.persistent._file_page
            idx = 0
            if page == "auto":
                idx = 0
            elif page == "quick":
                idx = 1 if autoEnabled else 0
            else:
                idx = configOffset + int(page) - 1

            maxNum = (configOffset + max) if max is not None else None
            target = idx + count

            if maxNum is not None:
                if wrap:
                    target %= maxNum
                elif target < 0 or target >= maxNum:
                    target = None
            elif target < 0:
                target = None

            if target is None:
                page = None
            elif target < configOffset:
                page = "auto" if (autoEnabled and target == 0) else "quick"
            else:
                page = str((target - configOffset) + 1)

            self.Page = page


        def __call__(self):
            if not self.get_sensitive():
                return

            renpy.store.persistent._file_page = self.Page
            renpy.restart_interaction()


        def get_sensitive(self):
            return self.Page is not None


        def predict(self):
            renpy.store._predict_file_page(self.Page)
