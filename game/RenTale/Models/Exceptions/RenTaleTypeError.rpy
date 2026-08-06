init -200 python in rentale:
    class RenTaleTypeError(TypeError):
        def __init__(self, expected, got):
            expectedStr = ""
            gotStr = got.__name__.capitalize()

            if isinstance(expected, tuple):
                parts = list()
                for t in expected:
                    parts.append(f"'{t.__name__.capitalize()}'")

                expectedStr = " or ".join(parts)
            else:
                expectedStr = f"'{expected.__name__.capitalize()}'"

            super().__init__(f"Expected {expectedStr}, got {gotStr}")
