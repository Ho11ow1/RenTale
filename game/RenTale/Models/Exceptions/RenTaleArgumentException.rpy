init -200 python in rentale:
    class RenTaleArgumentException(Exception):
        def __init__(self, message):
            super().__init__(message)
