init -100 python:
    class Event():
        def __init__(self, name, location, isUnlocked = False, isAutomatic = False, isCompleted = False, unlockCondition = None, action = None):
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(location) != Location:
                raise RenTaleTypeError(Location, type(location))
            if type(isUnlocked) != bool:
                raise RenTaleTypeError(bool, type(isUnlocked))
            if type(isAutomatic) != bool:
                raise RenTaleTypeError(bool, type(isAutomatic))
            if unlockCondition is not None and type(unlockCondition) != str:
                raise RenTaleTypeError((str, type(None)), type(unlockCondition))
            if action is not None and type(action) != str:
                raise RenTaleTypeError((str, type(None)), type(action))

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
