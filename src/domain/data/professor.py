from src.domain.data.base import DataEntity, DataException
from src.domain.data.document import Document
from src.domain.view.factory import material_card, title, sub_title, break_line, image


class Professor(DataEntity):
    def __init__(self,
                 full_name: str,
                 title: str,
                 personal_email: str,
                 faculty_email: str,
                 office_hours_timeframe: str,
                 office_hours_location: str,
                 profile_img: Document,
                 additional_info: Document,
                 ):
        super(Professor, self).__init__(0)
        self.personal_email = personal_email
        self.faculty_email = faculty_email
        self.title = title
        self.full_name = full_name
        self.office_hours_timeframe = office_hours_timeframe
        self.office_hours_location = office_hours_location
        self.profile_img = profile_img
        self.additional_info = additional_info

    @staticmethod
    def from_csv(csv_string: str):
        csv_list = csv_string.strip().split(",")
        if len(csv_list) != 9: raise DataException("Invalid CSV Format")
        professor = Professor(
            csv_list[1],
            csv_list[2],
            csv_list[3],
            csv_list[4],
            csv_list[5],
            csv_list[6],
            Document.from_csv(csv_list[7]),
            Document.from_csv(csv_list[8]),
        )
        professor.set_id(int(csv_list[0]))
        return professor

    def to_csv(self) -> str:
        return f"{self.get_id()},{self.full_name},{self.title}," \
               f"{self.personal_email},{self.faculty_email}," \
               f"{self.office_hours_timeframe},{self.office_hours_location}," \
               f"{self.profile_img.to_csv()},{self.additional_info.to_csv()}"

    def to_html(self) -> str:
        content = title(f"{self.title}, {self.full_name}") + break_line + \
                  sub_title(f"Personal email: {self.personal_email}") + \
                  sub_title(f"Faculty email: {self.faculty_email}") + \
                  sub_title(f"Office hours: {self.office_hours_timeframe}, {self.office_hours_location}") + \
                  image(self.profile_img.location) + \
                  self.additional_info.to_html()
        return material_card(content)

    def __str__(self) -> str:
        return f"{self.title}, {self.full_name}\n" \
               f"Personal email: {self.personal_email}\n" \
               f"Faculty email: {self.faculty_email}\n" \
               f"Office hours: {self.office_hours_timeframe}, {self.office_hours_location}\n" \
               f"Profile image {self.profile_img}\n" \
               f"Additional information {self.additional_info}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Professor) and super().__eq__(other)
