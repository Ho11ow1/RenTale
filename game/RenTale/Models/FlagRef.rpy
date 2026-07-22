init -100 python in rentale:
    class FlagRef():
        def __init__(self, name: str, value: int | bool):
            """
            Type-safe flag wrapper. Accepts Int or Bool. Type is locked on creation.
            """
            if type(name) != str:
                raise RenTaleTypeError(str, type(name))
            if type(value) not in (int, bool):
                raise RenTaleTypeError((int, bool), type(value))

            self.name = name
            self.value = value

            all_flags[name] = self


        def set(self, value: int | bool) -> None:
            """
            Sets the 'value' variable to the passed in 'value'
            """
            if type(value) != type(self.value):
                raise RenTaleTypeError(type(self.value), type(value))
            
            self.value = value


        def toggle(self) -> None:
            """
            Toggles the 'value' from false to true and vice versa
            """
            if type(self.value) != bool:
                raise RenTaleArgumentException("Cannot toggle an 'Int' flag")

            self.value = not self.value


        def increment(self, amount: int = 1) -> None:
            """
            Increases the 'value' by the given 'amount'
            """
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            if type(self.value) != int:
                raise RenTaleArgumentException("Cannot increment a 'Bool' flag")

            self.set(self.value + amount)

        
        def decrement(self, amount: int = 1) -> None:
            """
            Decreases the 'value' by the given 'amount'
            """
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            if type(self.value) != int:
                raise RenTaleArgumentException("Cannot decrement a 'Bool' flag")

            self.set(self.value - amount)
