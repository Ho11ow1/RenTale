init -10 python in rentale:
    class FilePageJump(renpy.store.Action):
        """
        Allows jumping multiple pages in the save & load screen
        """
        def __init__(self, max: int | None = None, wrap: bool = False, auto: bool = True, quick: bool = True, step: int = 1):
            if max is not None and type(max) != int:
                raise RenTaleTypeError((int, type(None)), type(max))
            if type(wrap) != bool:
                raise RenTaleTypeError(bool, type(wrap))
            if type(auto) != bool:
                raise RenTaleTypeError(bool, type(auto))
            if type(quick) != bool:
                raise RenTaleTypeError(bool, type(quick))
            if type(step) != int:
                raise RenTaleTypeError(int, type(step))
            if step == 0:
                return


            autoEnabled = renpy.config.has_autosave and auto
            quickEnabled = renpy.config.has_quicksave and quick
            selected = renpy.store.persistent._file_page
            chapter = renpy.store.persistent._file_chapter
            jump = abs(step) == 10
            target = None


            if jump:
                offset = ((int(selected) - 1) % 10) + 1 if unicode(selected).isnumeric() else 1
                
                if step > 0:
                    target = (chapter + 1) * 10 + offset
                    if max is not None and target > max:
                        target = 1 if wrap else max
                else:
                    target = (chapter - 1) * 10 + offset
                    if max is not None and target < 0:
                        target = max if wrap else 1
            else:
                if selected not in ("auto", "quick"):
                    target = int(selected) + step

                    if max is not None:
                        if target > max:
                            if wrap:
                                target = "auto" if autoEnabled else "quick" if quickEnabled else None
                            else:
                                target = max
                        elif target < 1:
                            target = max if wrap else "quick" if quickEnabled else "auto" if autoEnabled else None
                    else:
                        if target < 1:
                            target = "quick" if quickEnabled else "auto" if autoEnabled else None


            if target is None:
                if selected == "auto":
                    if step > 0 and quickEnabled:
                        target = "quick"
                    elif step < 0:
                        target = max if wrap else None 

                elif selected == "quick":
                    if step > 0:
                        target = "1"
                    elif step < 0 and autoEnabled:
                        target = "auto"
                    else:
                        target = max if wrap else None


            self.Page = str(target) if target is not None else None


        def __call__(self):
            if not self.get_sensitive():
                return

            if unicode(self.Page).isnumeric():
                renpy.store.persistent._file_chapter = _calc_chapter(int(self.Page))

            renpy.store.persistent._file_page = self.Page
            renpy.restart_interaction()


        def get_sensitive(self):
            return self.Page is not None


        def predict(self):
            renpy.store._predict_file_page(self.Page)
