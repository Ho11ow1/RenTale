init 1 python:
    class FlagRef:
        def __init__(self, value):
            if value is None:
                raise ValueError(f"FlagRef value cannot be None")
            if type(value) not in (int, bool):
                raise TypeError(f"FlagRef value type must be int or bool, got {type(value).__name__}")

            self.value = value

