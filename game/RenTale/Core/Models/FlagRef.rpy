init -100 python:
    class FlagRef():
        def __init__(self, value):
            if type(value) not in (int, bool):
                raise RenTaleTypeError((int, bool), type(value))

            self.Value = value


        def Set(self, value: int | bool) -> None:
            if type(value) != type(self.Value):
                raise RenTaleTypeError(type(self.Value), type(value))
            
            self.Value = value


        def Toggle(self) -> None:
            if type(self.Value) != bool:
                raise RenTaleArgumentException("Cannot toggle an 'Int' flag")

            self.Value = not self.Value


        def Increment(self, amount: int = 1) -> None:        
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            if type(self.Value) != int:
                raise RenTaleArgumentException("Cannot increment a 'Bool' flag")

            self.Set(self.Value + amount)

        
        def Decrement(self, amount: int = 1) -> None:        
            if type(amount) != int:
                raise RenTaleTypeError(int, type(amount))
            if type(self.Value) != int:
                raise RenTaleArgumentException("Cannot decrement a 'Bool' flag")

            self.Set(self.Value - amount)
