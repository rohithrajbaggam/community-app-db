from enum import Enum

class ExamModeEnumType(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    OTHERS = "OTHERS"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


