from enum import Enum

class UserStatusEnumType(Enum):
    NOSTARTED = "NOSTARTED"
    INPROGRESS = "INPROGRESS"
    INCOMPELETED = "COMPELETED"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]