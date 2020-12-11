from src.domain.data.base import DataEntity


class Course(DataEntity):
    def __init__(self, id,
                 ):
        super(Course, self).__init__(id)

    def to_html(self) -> str:
        pass

    def __str__(self):
        pass

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Course):
            return super().__eq__(other)
        return False

