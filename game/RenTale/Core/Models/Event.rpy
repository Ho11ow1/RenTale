init -100 python:
    class Event():
        def __init__(self, name, location, isUnlocked = False, isAutomatic = False, isCompleted = False, unlockCondition = None, action = None):
            """
            Represents a game event tied to a Location. Automatically registers into RenTale_All_Locations at the given location on creation.
            """
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
            self.UnlockCondition = RenTale_sanitize_string(unlockCondition)
            self.Action = RenTale_sanitize_string(action)

            RenTale_All_Locations[self.Location].append(self)


        def Unlock(self) -> None:
            """
            Sets the 'IsUnlocked' variable to true if not already true
            """
            if not self.IsUnlocked:
                self.IsUnlocked = True


        def CheckCondition(self) -> bool:
            """
            Returns true if the 'UnlockCondition' is None or evaluates to true
            """
            if self.UnlockCondition is None:
                return True

            return eval(self.UnlockCondition)


        def Play(self) -> None:
            """
            Executes actions in the 'Action' variable in order(LTR), split via ';' if not None and not already completed
            """
            if self.IsCompleted:
                return

            self.IsCompleted = True

            if self.Action is not None:
                actions = self.Action.split(';')

                for action in actions:
                    exec(action.strip())
