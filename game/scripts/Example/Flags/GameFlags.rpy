init -100 python:

    class willowFlags():
        def __init__(self):
            self.HaveMet = rentale.FlagRef("Willow.HaveMet", False)


    class aliceFlags():
        def __init__(self):
            self.HaveMet = rentale.FlagRef("Alice.HaveMet", False)


default WillowFlags = willowFlags()
default AliceFlags = aliceFlags()
