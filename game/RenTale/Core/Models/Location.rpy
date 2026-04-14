init -100 python:
    class Location():
        def __init__(self, name, label, isUnlocked = True):
            """
            Represents a navigable game location. Automatically registers into RenTale_All_Locations on creation.
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

            store.RenTale_All_Locations[self] = list()


        def Unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true if not already true
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True
