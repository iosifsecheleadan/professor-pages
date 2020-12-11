from src.domain.data.base import DataEntity


class Announcement(DataEntity):
    def __init__(self, id,
                 ):
        super(Announcement, self).__init__(id)

    def to_html(self) -> str:
        pass

    def __str__(self):
        pass

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Announcement):
            return super().__eq__(other)
        return False

