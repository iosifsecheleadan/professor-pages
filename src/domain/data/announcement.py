from datetime import datetime
from enum import Enum

from src.domain.data.base import DataEntity, DataException
from src.domain.data.document import Document
from src.domain.view.color import white, green, light_green, red, light_red, black
from src.domain.view.factory import material_card, sub_title


class Type(Enum): NORMAL, IMPORTANT, VERY_IMPORTANT = 0, 1, 2


class Announcement(DataEntity):
    def __init__(self, identifier: int,
                 title: str,
                 document: Document,
                 announcement_type: Type = Type.NORMAL,
                 ):
        super(Announcement, self).__init__(identifier)
        self.time = datetime.now().strftime("%c")
        self.title = title
        self.document = document
        self.type = announcement_type

    @staticmethod
    def from_csv(csv_string: str):
        csv_list = csv_string.strip().split(",")
        if len(csv_list) != 4: raise DataException("Invalid CSV Format")
        return Announcement(
            int(csv_list[0]),
            csv_list[1],
            Document.from_csv(csv_list[2]),
            Type(int(csv_list[3]))
        )

    def to_csv(self) -> str:
        return f"{self.get_id()},{self.title},{self.document.to_csv()},{self.type.value}"

    def to_html(self) -> str:
        color = black
        background = white
        italics = False
        if self.type == Type.IMPORTANT:
            color = green
            background = light_green
        if self.type == Type.VERY_IMPORTANT:
            color = red
            background = light_red
            italics = True

        content = sub_title(self.title, color=color, italics=italics)
        content += self.document.to_html()
        return material_card(content, color=background)

    def __str__(self) -> str:
        return f"{str(self.type.name).title()} Announcement : {self.title}\n" \
               f"Announcement {self.document}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Announcement) and super().__eq__(other)
