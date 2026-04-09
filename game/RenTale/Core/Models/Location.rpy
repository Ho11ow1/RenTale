init -100 python:
    class Location():
        def __init__(self, name, label, isUnlocked = True):
            if type(name) != str:
                raise TypeError(f"Expected 'String', got '{type(name).__name__}'")
            if type(label) != str:
                raise TypeError(f"Expected 'String', got '{type(label).__name__}'")
            if type(isUnlocked) != bool:
                raise TypeError(f"Expected 'Bool', got '{type(isUnlocked).__name__}'")

            self.Name = name
            self.Label = label
            self.IsUnlocked = isUnlocked
            RenTale_ALL_LOCATIONS[self] = []


        def Unlock(self) -> None:
            if not self.IsUnlocked:
                self.IsUnlocked = True
