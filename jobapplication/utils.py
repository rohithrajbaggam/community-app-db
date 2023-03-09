from enum import Enum

class JobModeEnumType(Enum):
    ONSITE = "ONSITE"
    REMOTE = "REMOTE"
    HYBRID = "HYBRID"
    OTHERS = "OTHERS"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


