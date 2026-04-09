init -10 python:
    class SkipTime(Action):
        def __init__(self, count: int = 1):
            if type(count) != int:
                raise TypeError(f"Expected 'Int', got '{type(count).__name__}'")

            self.count = count


        def __call__(self):
            RenTale_advance_time(self.count)
            renpy.call("RenTale_Time_Null", from_current = True)
