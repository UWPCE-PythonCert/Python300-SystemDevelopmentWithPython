class ConstrainedInt(int):
    """keeps value between 0 and 255"""
    def __new__(cls, value):
        value = value % 255
        self = int.__new__(cls, value)
        return self
