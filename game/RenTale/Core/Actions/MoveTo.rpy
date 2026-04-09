init -10 python:
    class MoveTo(Action):
        def __init__(self, location):
            if type(location) != Location:
                raise TypeError(f"Expected 'Location', got '{type(location).__name__}'")

            self.Location = location


        def __call__(self):
            RenTale_GoTo(self.Location)
