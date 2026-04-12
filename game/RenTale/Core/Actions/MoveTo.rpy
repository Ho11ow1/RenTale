init -10 python:
    class MoveTo(Action):
        def __init__(self, location):
            if type(location) != Location:
                raise RenTaleTypeError(Location, type(location))

            self.Location = location


        def __call__(self):
            RenTale_GoTo(self.Location)
