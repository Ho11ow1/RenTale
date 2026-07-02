init -200 python in rentale:
    class RenTaleValueError(ValueError):
        def __init__(self, expected, got):
            super().__init__(f"Expected '{expected}', got '{got}'")
