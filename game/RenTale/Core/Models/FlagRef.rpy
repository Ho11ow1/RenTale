init -100 python:
    class FlagRef():
        def __init__(self, value):
            """
            Type-safe flag wrapper. Accepts Int or Bool. Type is locked on creation.
            """
            if type(value) not in (int, bool):
                raise RenTaleTypeError((int, bool), type(value))

            self.Value = value


        def Set(self, value: int | bool) -> None:
            """
            Sets the 'Value' variable to the passed in 'value'
            """
            if type(value) != type(self.Value):
                raise RenTaleTypeError(type(self.Value), type(value))
            
            self.Value = value


        def Toggle(self) -> None:
            """
            Toggles the 'Value' from false to true and vice versa
            """
            if type(self.Value) != bool:
                raise RenTaleArgumentException("Cannot toggle an 'Int' flag")

            self.Value = not self.Value


        def Increment(self, amount: int = 1) -> None:
            """
            Increases the 'Value' by the given 'amount'
            """
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            if type(self.Value) != int:
                raise RenTaleArgumentException("Cannot increment a 'Bool' flag")

            self.Set(self.Value + amount)

        
        def Decrement(self, amount: int = 1) -> None:
            """
            Decreases the 'Value' by the given 'amount'
            """
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            if type(self.Value) != int:
                raise RenTaleArgumentException("Cannot decrement a 'Bool' flag")

            self.Set(self.Value - amount)
