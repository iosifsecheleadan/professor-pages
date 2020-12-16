from src.domain.data.base import DataEntity, DataException
from src.domain.data.document import Document
from src.domain.view.factory import material_card, text


class CourseWeek(DataEntity):
    def __init__(self, identifier: int,
                 course_identifier: int,
                 week_number: int,
                 documents: list,
                 ):
        super(CourseWeek, self).__init__(identifier)
        self.course_identifier = course_identifier
        self.week_number = week_number
        self.documents = documents

    @staticmethod
    def from_csv(csv_string: str):
        csv_list = csv_string.strip().split(",")
        if len(csv_list) < 4: raise DataException("Invalid CSV Format")
        document_list = []
        for document_location in csv_list[3:]:
            document_list.append(Document.from_csv(document_location))
        return CourseWeek(
            int(csv_list[0]),
            int(csv_list[1]),
            int(csv_list[2]),
            document_list
        )

    def to_csv(self) -> str:
        csv = f"{self.get_id()},{self.course_identifier},{self.week_number}"
        for document in self.documents:
            csv += f",{document.to_csv()}"
        return csv

    def to_html(self) -> str:
        return material_card(content=text(
                str(self).replace("\n", " <br> ")
            ))

    def __str__(self) -> str:
        string = ""
        if self.week_number == 0: string += "About"
        else: string += f"Week {self.week_number}"
        for document in self.documents:
            string += f"\n{document}"
        return string

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CourseWeek) and super().__eq__(other)

