from src.domain.data.about import About
from src.domain.data.announcement import Announcement
from src.domain.data.course import Course
from src.domain.data.course_week import CourseWeek
from src.domain.data.document import Document
from src.domain.data.professor import Professor


class DataFactory:
    @staticmethod
    def about_from_csv(csv_string):
        return About.from_csv(csv_string)

    @staticmethod
    def basic_about():
        return About([])

    @staticmethod
    def announcement_from_csv(csv_string):
        return Announcement.from_csv(csv_string)

    @staticmethod
    def basic_announcement():
        return Announcement("title",
                            Document.from_csv("what.txt")
                            )

    @staticmethod
    def course_from_csv(csv_string):
        return Course.from_csv(csv_string)

    @staticmethod
    def basic_course():
        return Course("name", "code", "faculty", 0, 0)

    @staticmethod
    def course_week_from_csv(csv_string):
        return CourseWeek.from_csv(csv_string)

    @staticmethod
    def basic_course_week():
        return CourseWeek(0, 0, [])

    @staticmethod
    def professor_from_csv(csv_string):
        return Professor.from_csv(csv_string)

    @staticmethod
    def basic_professor():
        return Professor("full name", "title",
                         "personal email", "faculty email",
                         "office hours time", "office hours location",
                         Document.from_csv("what.png"), Document.from_csv("what.txt")
                         )

    @staticmethod
    def document_from_csv(csv_string):
        return Document.from_csv(csv_string)
