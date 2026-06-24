init -200 python:
    class RenTaleArgumentException(Exception):
        def __init__(self, message):
            super().__init__(message)
