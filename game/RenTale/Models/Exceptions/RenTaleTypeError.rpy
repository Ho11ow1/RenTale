init -200 python:
    TYPE_NAMES = {
        NoneType: "'None'",
        int: "'Int'",
        float: "'Float'",
        bool: "'Bool'",
        str: "'String'",
        dict: "'Dictionary'",
        list: "'List'",
        set: "'Set'"
    }

    class RenTaleTypeError(TypeError):
        def __init__(self, expected, got):
            expectedStr = ""
            gotStr = TYPE_NAMES.get(got, got.__name__.capitalize())

            if isinstance(expected, tuple):
                parts = list()
                for t in expected:
                    parts.append(TYPE_NAMES.get(t, t.__name__.capitalize()))

                expectedStr = " or ".join(parts)
            else:
                expectedStr = TYPE_NAMES.get(expected, expected.__name__.capitalize())

            super().__init__(f"Expected {expectedStr}, got {gotStr}")
