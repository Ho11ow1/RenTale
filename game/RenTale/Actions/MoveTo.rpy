init -10 python in rentale:
    class MoveTo(renpy.store.Action):
        """
        Moves to a given location(Location) if it exists and is unlocked
        """
        def __init__(self, location: Location):
            if type(location) != Location:
                raise RenTaleTypeError(Location, type(location))

            self.Location = location


        def __call__(self):
            go_to(self.Location)
