init -10 python:
    class SkipTime(Action):
        """
        Skips forward in time by the given amount of time periods (1 by default)
        """
        def __init__(self, count: int = 1):
            if type(count) != int:
                raise RenTaleTypeError(int, type(count))

            self.Count = count


        def __call__(self):
            RenTale_Advance_Time(self.Count)
            renpy.call("RenTale_Time_Null", from_current = True)
