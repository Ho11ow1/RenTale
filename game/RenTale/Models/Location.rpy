init -100 python in rentale:
    class Location():
        def __init__(self, name, label, isUnlocked = True):
            """
            Represents a navigable game location. Automatically registers into rentale.all_locations on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(label) != str:
                raise RenTaleTypeError(str, type(label))
            if type(isUnlocked) != bool:
                raise RenTaleTypeError(bool, type(isUnlocked))

            self.Name = name
            self.Label = label
            self.IsUnlocked = isUnlocked

            all_locations[self] = list()


        def unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true if not already true
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True
