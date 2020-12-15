from src.domain.data.about import About
from src.domain.data.announcement import Announcement
from src.domain.data.course import Course
from src.domain.data.course_week import CourseWeek
from src.domain.data.professor import Professor


class DataFactory:
    @staticmethod
    def about_from_csv(csv_string):
        return About.from_csv(csv_string)

    @staticmethod
    def announcement_from_csv(csv_string):
        return Announcement.from_csv(csv_string)

    @staticmethod
    def course_from_csv(csv_string):
        return Course.from_csv(csv_string)

    @staticmethod
    def course_week_from_csv(csv_string):
        return CourseWeek.from_csv(csv_string)

    @staticmethod
    def professor_from_csv(csv_string):
        return Professor.from_csv(csv_string)
