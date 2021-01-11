from src.domain.data.base import DataEntity, DataException


from src.domain.data.document import Document


# todo add repository method : add_about_document
from src.domain.view.factory import material_card, title


class About(DataEntity):
    def __init__(self,
                 documents: list,
                 ):
        super(About, self).__init__(0)
        self.documents = documents

    @staticmethod
    def from_csv(csv_string: str):
        csv_list = csv_string.strip().split(",")
        if len(csv_list) < 2: raise DataException("Invalid CSV Format")
        document_list = []
        for document_location in csv_list[1:]:
            document_list.append(Document.from_csv(document_location))
        about = About(document_list)
        about.set_id(int(csv_list[0]))
        return about

    def to_csv(self) -> str:
        csv = str(self.get_id())
        for document in self.documents:
            csv += f",{document.to_csv()}"
        return csv

    def to_html(self) -> str:
        content = title("About")
        for document in self.documents:
            content += document.to_html()
        return material_card(content)

    def __str__(self) -> str:
        string = "About Documents:"
        for document in self.documents:
            string += f"\nAbout {document}"
        return string

    def __eq__(self, other: object) -> bool:
        return isinstance(other, About) and super().__eq__(other)
