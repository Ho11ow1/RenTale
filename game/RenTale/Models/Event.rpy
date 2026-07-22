init -100 python in rentale:
    class Event():
        def __init__(self, name: str, location, label: str, is_unlocked: bool = False, is_automatic: bool = False, is_completed: bool = False, unlock_condition: bool | None = None):
            """
            Represents a game event tied to a Location. Automatically registers into rentale.all_locations at the given location on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(location) != Location:
                raise RenTaleTypeError(Location, type(location))
            if type(label) != str:
                raise RenTaleTypeError(str, type(label))
            if label not in renpy.get_all_labels():
                raise RenTaleArgumentException(f"Label '{label}' is not defined.")
            if type(is_unlocked) != bool:
                raise RenTaleTypeError(bool, type(is_unlocked))
            if type(is_automatic) != bool:
                raise RenTaleTypeError(bool, type(is_automatic))
            if type(is_completed) != bool:
                raise RenTaleTypeError(bool, type(is_completed))
            if unlock_condition is not None and type(unlock_condition) != str:
                raise RenTaleTypeError((str, type(None)), type(unlock_condition))

            self.name = name
            self.location = location
            self.label = label
            self.is_unlocked = is_unlocked
            self.is_automatic = is_automatic
            self.is_completed = is_completed
            self.unlock_condition = _sanitize_string(unlock_condition)

            all_locations[self.location].append(self)


        def unlock(self) -> None:
            """
            Sets the 'is_unlocked' variable to true if not already true
            """
            if not self.is_unlocked:
                self.is_unlocked = True


        def check_condition(self) -> bool:
            """
            Returns true if the 'unlock_condition' is None or evaluates to True
            """
            if self.unlock_condition is None:
                return True

            return eval(self.unlock_condition, vars(renpy.store))


        def play(self) -> None:
            """
            Calls the associated Ren'Py label if the event has not been completed and the unlock_condition is None or evaluates to True
            """
            if self.is_completed or not self.check_condition():
                return

            self.is_completed = True

            renpy.call(self.label)
