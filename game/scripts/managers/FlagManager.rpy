init -1 python:
    class FlagManager:
        def Set(flagRef, value):
            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")

            oldVal = flagRef.value
            if type(value) != type(oldVal):
                raise TypeError(f"Expected {type(oldVal).__name__}, got {type(value).__name__}")

            flagRef.value = value


        def Get(flagRef):
            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")

            return flagRef.value


        @classmethod
        def Increment(cls, flagRef, amount = 1):
            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")
            if type(amount) != int:
                raise TypeError(f"Expected int, got {type(amount).__name__}")

            val = cls.Get(flagRef)

            if type(val) != int:
                raise TypeError(f"Cannot increment non-numeric flag. Current value is {type(val).__name__}: {val}")

            cls.Set(flagRef, val + amount)
