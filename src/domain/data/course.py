from src.domain.data.base import DataEntity, DataException
from src.domain.view.factory import material_card, text


class Course(DataEntity):
    def __init__(self, identifier: int,
                 name: str,
                 code: str,
                 faculty: str,
                 study_year: int,
                 no_weeks: int,
                 ):
        super(Course, self).__init__(identifier)
        self.name = name
        self.code = code
        self.faculty = faculty
        self.study_year = study_year
        self.no_weeks = no_weeks

    @staticmethod
    def from_csv(csv_string: str):
        csv_list = csv_string.strip().split(",")
        if len(csv_list) != 6: raise DataException("Invalid CSV Format")
        return Course(
            int(csv_list[0]),
            csv_list[1],
            csv_list[2],
            csv_list[3],
            int(csv_list[4]),
            int(csv_list[5]),
        )

    def to_csv(self) -> str:
        return f"{self.get_id()},{self.name},{self.code},{self.faculty}," \
               f"{self.study_year},{self.no_weeks}"

    def to_html(self) -> str:
        return material_card(content=text(
                str(self).replace("\n", " <br> ")
            ))

    def __str__(self) -> str:
        return f"{self.name} ({self.code})\n" \
               f"{self.no_weeks} week course for year {self.study_year} students at {self.faculty}."

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Course) and super().__eq__(other)

