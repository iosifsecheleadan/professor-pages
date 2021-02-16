from os.path import normpath

from src.ctrl.controller import WebControllerInterface
from src.domain.data.course import Course
from src.domain.data.course_week import CourseWeek
from src.domain.data.factory import DataFactory
from src.domain.view.factory import link_text
from src.domain.view.page import page
from src.repo.course import CourseRepository
from src.repo.course_week import CourseWeekRepository


class CourseController(WebControllerInterface):
    def __init__(self):
        self.courses_directory = normpath("../page/courses/")
        self.all_courses_page_location = normpath("../page/all_courses.html")
        self.Courses = CourseRepository()
        self.CourseWeeks = CourseWeekRepository()

    def add_course(self, course: Course):
        self.Courses.create(course)

    def update_course(self, course: Course):
        self.Courses.update(course)

    def remove_course(self, course: Course):
        self.Courses.delete(course)
        self.CourseWeeks.delete_course(course.get_id())

    def add_course_week(self, course_week: CourseWeek, course: Course):
        course_week.course_identifier = course.get_id()
        self.CourseWeeks.create(course_week)

    def update_course_week(self, course_week: CourseWeek):
        self.CourseWeeks.update(course_week)

    def remove_course_week(self, course_week: CourseWeek):
        self.CourseWeeks.delete(course_week)

    def get_by_name(self, name):
        return self.Courses.getByName(name)

    def get_by_code(self, code):
        return self.Courses.getByCode(code)

    def get_by_week(self, c_identif, week_nr):
        return self.CourseWeeks.getByWeek(c_identif,week_nr)

    def get_by_course(self, c_identif):
        return self.CourseWeeks.getByCourse(c_identif)

    def save(self):
        self.Courses.save_all()
        self.CourseWeeks.save_all()
        self._create_pages()

    def _create_pages(self):
        course_page_location=[]
        for course in self.Courses.courses:
            weeks = [course]
            for course_week in self.CourseWeeks.weeks:
                if course_week.course_identifier == course.get_id():
                    weeks.append(course_week)
            document = DataFactory.document_from_csv(normpath(f"{self.courses_directory}/{course.name}.html"))
            with open(document.location, "w") as file:
                file.write( page(weeks, True) )
            course_page_location.append(document.to_html())
        with open(normpath(self.all_courses_page_location), "w") as file:
            file.write(page(course_page_location))


