init -100 python in rentale:
    class Event():
        def __init__(self, name, location, label, isUnlocked = False, isAutomatic = False, isCompleted = False, unlockCondition = None):
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
            if type(isUnlocked) != bool:
                raise RenTaleTypeError(bool, type(isUnlocked))
            if type(isAutomatic) != bool:
                raise RenTaleTypeError(bool, type(isAutomatic))

            self.Name = name
            self.Location = location
            self.Label = label
            self.IsUnlocked = isUnlocked
            self.IsAutomatic = isAutomatic
            self.IsCompleted = isCompleted
            self.UnlockCondition = _sanitize_string(unlockCondition)

            all_locations[self.Location].append(self)


        def unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true if not already true
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True


        def check_condition(self) -> bool:
            """
            Returns true if the 'UnlockCondition' is None or evaluates to True
            """
            if self.UnlockCondition is None:
                return True

            return eval(self.UnlockCondition, vars(renpy.store))


        def play(self) -> None:
            """
            Calls the associated Ren'Py label if the event has not been completed and the UnlockCondition is None or evaluates to True
            """
            if self.IsCompleted or not self.check_condition():
                return

            self.IsCompleted = True

            renpy.call(self.Label)
