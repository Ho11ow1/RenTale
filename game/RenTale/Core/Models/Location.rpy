init -100 python:
    class Location():
        def __init__(self, name, label, isUnlocked = True):
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(label) != str:
                raise RenTaleTypeError(str, type(label))
            if type(isUnlocked) != bool:
                raise RenTaleTypeError(bool, type(isUnlocked))

            self.Name = name
            self.Label = label
            self.IsUnlocked = isUnlocked
            
            RenTale_All_Locations[self] = []


        def Unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true if not already true
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True
