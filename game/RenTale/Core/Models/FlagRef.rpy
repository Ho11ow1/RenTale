init -100 python:
    class FlagRef():
        def __init__(self, value):
            self.Value = value


        def __setattr__(self, name, value):
            if name == "Value" and hasattr(self, "Value"):
                if value is None:
                    raise ValueError(f"FlagRef value cannot be None")
                if type(value) not in (int, bool):
                    raise TypeError(f"FlagRef value type must be int or bool, got {type(value).__name__}")
                if type(value) != type(self.Value):
                    raise TypeError(f"Expected {type(self.Value).__name__}, got {type(value).__name__}")

            super().__setattr__(name, value)


        def Set(self, value: int | bool) -> None:
            if type(value) != type(self.Value):
                raise TypeError(f"Expected {type(self.Value).__name__}, got {type(value).__name__}")
            
            self.Value = value


        def Toggle(self) -> None:
            if type(self.Value) != bool:
                raise TypeError(f"Expected bool, got {type(self.Value).__name__}")

            self.Value = not self.Value


        def Increment(self, amount: int = 1) -> None:        
            if type(amount) != int:
                raise TypeError(f"Expected int, got {type(amount).__name__}")
            if type(self.Value) != int:
                raise TypeError(f"Cannot increment non-numeric flag. Current value type is {type(self.Value).__name__}: {self.Value}")

            self.Set(self.Value + amount)

        
        def Decrement(self, amount: int = 1) -> None:        
            if type(amount) != int:
                raise TypeError(f"Expected int, got {type(amount).__name__}")
            if type(self.Value) != int:
                raise TypeError(f"Cannot decrement non-numeric flag. Current value type is {type(self.Value).__name__}: {self.Value}")

            self.Set(self.Value - amount)
