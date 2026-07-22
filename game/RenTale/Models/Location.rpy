init -100 python in rentale:
    class Location():
        def __init__(self, name: str, label: str, is_unlocked: bool = True):
            """
            Represents a navigable game location. Automatically registers into rentale.all_locations on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(label) != str:
                raise RenTaleTypeError(str, type(label))
            if label not in renpy.get_all_labels():
                raise RenTaleArgumentException(f"Label '{label}' is not defined.")
            if type(is_unlocked) != bool:
                raise RenTaleTypeError(bool, type(is_unlocked))

            self.name = name
            self.label = label
            self.is_unlocked = is_unlocked

            all_locations[self] = list()


        def unlock(self) -> None:
            """
            Sets the 'is_unlocked' variable to true if not already true
            """
            if not self.is_unlocked:
                self.is_unlocked = True
