init -100 python:
    class Event():
        def __init__(self, name, location, isUnlocked = False, isAutomatic = False, isCompleted = False, unlockCondition = None, action = None):
            if type(name) != str:
                raise TypeError(f"Expected 'String', got '{type(name).__name__}'")
            if type(location) != Location:
                raise TypeError(f"Expected 'Location', got '{type(location).__name__}'")
            if type(isUnlocked) != bool:
                raise TypeError(f"Expected 'Bool', got '{type(isUnlocked).__name__}'")
            if type(isAutomatic) != bool:
                raise TypeError(f"Expected 'Bool', got '{type(isAutomatic).__name__}'")
            if unlockCondition is not None and type(unlockCondition) != str:
                raise TypeError(f"Expected 'String' or 'None', got '{type(unlockCondition).__name__}'")
            if action is not None and type(action) != str:
                raise TypeError(f"Expected 'String' or 'None', got '{type(action).__name__}'")

            self.Name = name
            self.Location = location
            self.IsUnlocked = isUnlocked
            self.IsAutomatic = isAutomatic
            self.IsCompleted = isCompleted
            self.UnlockCondition = unlockCondition
            self.Action = action
            RenTale_All_Locations[self.Location].append(self)


        def Unlock(self) -> None:
            if not self.IsUnlocked:
                self.IsUnlocked = True


        def CheckCondition(self) -> bool:
            if self.UnlockCondition is None:
                return True
            
            return eval(self.UnlockCondition)


        def Play(self) -> None:
            self.IsCompleted = True

            if self.Action is not None:
                actions = self.Action.split(';')

                for action in actions:
                    exec(action.strip())
