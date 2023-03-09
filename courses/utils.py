from enum import Enum 

class CourseStatusEnum(Enum):
    NOTSTARTED = "NOTSTARTED"
    INPROGESS = "INPROGRESS"
    COMPELETED = "COMPELETED"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
