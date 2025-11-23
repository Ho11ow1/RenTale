init 1 python:
    class FlagManager:
        """
            Centralized singleton flag management system with runtime type validation.

            Provides type safe flag operations ensuring that FlagRef values are never invalid or.
            have unexpected values resulting in error.
        """

        def Set(flagRef: FlagRef, value: int | bool) -> None:
            """
                Sets a value for the passed in FlagRef.

                Args:
                    flagRef (FlagRef): The flag reference to return the value from.
                    value (int | bool): The value to set for the flagRef.

                Raises:
                    TypeError: If flagRef is not a FlagRef instance.
                    TypeError: If value is not the same type as flagRef's value.
            """

            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")
            if type(value) != type(flagRef.value):
                raise TypeError(f"Expected {type(flagRef.value).__name__}, got {type(value).__name__}")

            flagRef.value = value


        def Get(flagRef: FlagRef) -> int | bool:
            """
                Returns the current value of the passed in FlagRef.

                Args:
                    flagRef (FlagRef): The flag reference to return the value from.

                Raises:
                    TypeError: If flagRef is not a FlagRef instance.

                Returns:
                    int | bool: the current value of the flagRef.
            """

            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")

            return flagRef.value


        @classmethod
        def Increment(cls, flagRef: FlagRef, amount: int = 1) -> None:
            """
                Increments the given FlagRef's value by the specified amount or 1 by default.

                Args:
                    flagRef (FlagRef): The flag reference to increment.
                    amount (int, optional): The amount to increment the flagref's value by.

                Raises:
                    TypeError: If flagRef is not a FlagRef instance.
                    TypeError: If amount is not an int instance.
                    TypeError: If flagRef's value is not an int instance.
            """

            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")
            if type(amount) != int:
                raise TypeError(f"Expected int, got {type(amount).__name__}")
            if type(flagRef.value) != int:
                raise TypeError(f"Cannot increment non-numeric flag. Current value is {type(flagRef.value).__name__}: {flagRef.value}")

            cls.Set(flagRef, flagRef.value + amount)

        
        @classmethod
        def Decrement(cls, flagRef: FlagRef, amount: int = 1) -> None:
            """
                Decreases the given FlagRef's value by the specified amount or 1 by default.

                Args:
                    flagRef (FlagRef): The flag reference to decrement.
                    amount (int, optional): The amount to decrement the flagref's value by.

                Raises:
                    TypeError: If flagRef is not a FlagRef instance.
                    TypeError: If amount is not an int instance.
                    TypeError: If flagRef's value is not an int instance.
            """

            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")
            if type(amount) != int:
                raise TypeError(f"Expected int, got {type(amount).__name__}")
            if type(flagRef.value) != int:
                raise TypeError(f"Cannot decrement non-numeric flag. Current value is {type(flagRef.value).__name__}: {flagRef.value}")

            cls.Set(flagRef, flagRef.value - amount)


        @classmethod
        def Toggle(cls, flagRef: FlagRef) -> None:
            """
                Toggles a boolean FlagRef to its opposite value.

                Args:
                    flagRef (FlagRef): The flag reference to toggle.

                Raises:
                    TypeError: If flagRef is not a FlagRef instance.
                    TypeError: If flagRef's value is not a bool instance.
            """

            if type(flagRef) != FlagRef:
                raise TypeError(f"Expected FlagRef, got {type(flagRef).__name__}")
            if type(flagRef.value) != bool:
                raise TypeError(f"Expected bool, got {type(flagRef.value).__name__}")

            cls.Set(flagRef, not flagRef.value)

