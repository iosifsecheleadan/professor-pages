import os

from commonmark import commonmark

from src.domain.data.base import DataException
from src.domain.view.color import red
from src.domain.view.factory import link_text, material_card, description


class Document:
    def __init__(self, location: str):
        self.location = os.path.normpath(location)

    @staticmethod
    def from_csv(csv_string: str):
        csv_list = csv_string.strip().rsplit(".", 1)
        if len(csv_list) != 2: raise DataException("Invalid CSV Format - Document Extension")
        extension = csv_list[1]

        switch = {
            "md": MarkdownDocument(csv_string),
        }
        try: return switch[extension]
        except KeyError: return Document(csv_string)

    def to_csv(self) -> str:
        return self.location

    def to_html(self) -> str:
        doc_name = os.path.basename(self.location)
        return link_text(content=doc_name, link=self.location)

    def __str__(self) -> str:
        return f"document at {self.location}"

    def __eq__(self, other):
        return isinstance(other, Document) and self.location == other.location


class MarkdownDocument(Document):
    def __init__(self,
                 location: str):
        super().__init__(location)

    def to_html(self) -> str:
        try:
            with open(self.location, "r") as markdown:
                return material_card(commonmark(markdown.read()))
        except FileNotFoundError: return material_card(
            description(f"File {self.location} not found", color=red)
        )

    def __str__(self) -> str:
        return "md - " + super().__str__()

