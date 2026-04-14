init -100 python:

    class willowFlags():
        def __init__(self):
            self.HaveMet = FlagRef(False)


    class aliceFlags():
        def __init__(self):
            self.HaveMet = FlagRef(False)


default WillowFlags = willowFlags()
default AliceFlags = aliceFlags()
