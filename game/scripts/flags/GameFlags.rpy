init -10 python:
    class Flags:
        def __init__(self):
            self.Main = self.Main()
            self.Side = self.Side()
            self.Willow = self.Willow()
            self.Alice = self.Alice()
        
        # === MAIN QUEST FLAGS ===
        class Main:
            def __init__(self):
                self.MainEvent1 = FlagRef(False)
        
        # === SIDE QUEST FLAGS ===
        class Side:
            def __init__(self):
                self.SideEvent1 = FlagRef(False)
        
        # === CHARACTER FLAGS ===
        class Willow:
            def __init__(self):
                self.HaveMet = FlagRef(False)
        
        class Alice:
            def __init__(self):
                self.HaveMet = FlagRef(False)

