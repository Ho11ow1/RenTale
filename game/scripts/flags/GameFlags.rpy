init -1 python:
    class FlagRef:
        def __init__(self, value):
            if value is None:
                raise ValueError(f"FlagRef value cannot be None")
            if type(value) not in (int, bool):
                raise TypeError(f"FlagRef value type must be int or bool, got {type(value).__name__}")

            self.value = value

    class Flags:
        # === MAIN QUEST FLAGS ===
        class Main:
            event_main_1 = FlagRef(False)
            event_rep_s = FlagRef(False)


        # === SIDE QUEST FLAGS ===
        class Side:
            willow_event_1 = FlagRef(False)


        # === CHARACTER FLAGS ===
        class Willow:
            have_met = FlagRef(False)


