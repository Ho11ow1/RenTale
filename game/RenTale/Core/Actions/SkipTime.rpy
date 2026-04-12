init -10 python:
    class SkipTime(Action):
        def __init__(self, count: int = 1):
            if type(count) != int:
                raise RenTaleTypeError(int, type(count))

            self.Count = count


        def __call__(self):
            RenTale_advance_time(self.Count)
            renpy.call("RenTale_Time_Null", from_current = True)
