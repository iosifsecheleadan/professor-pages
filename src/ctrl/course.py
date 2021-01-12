from os.path import normpath

from src.ctrl.controller import WebControllerInterface
from src.domain.data.course import Course
from src.domain.data.course_week import CourseWeek
from src.domain.view.page import page
from src.repo.course import CourseRepository
from src.repo.course_week import CourseWeekRepository


class CourseController(WebControllerInterface):
    def __init__(self):
        self.courses_directory = normpath("../page/courses/")
        self.Courses = CourseRepository()
        self.CourseWeeks = CourseWeekRepository()

    def add_course(self, course: Course):
        self.Courses.create(course)

    def update_course(self, course: Course):
        self.Courses.update(course)

    def remove_course(self, course: Course):
        self.Courses.delete(course)

    def add_course_week(self, course_week: CourseWeek, course: Course):
        course_week.course_identifier = course.get_id()
        self.CourseWeeks.create(course_week)

    def update_course_week(self, course_week: CourseWeek):
        self.CourseWeeks.update(course_week)

    def remove_course_week(self, course_week: CourseWeek):
        self.CourseWeeks.delete(course_week)

    def getByName(self,name):
        self.Courses.getByName(name)

    def getByCode(self,code):
        self.Courses.getByCode(code)

    def getByWeek(self, c_identif, week_nr):
        self.CourseWeeks.getByWeek(c_identif,week_nr)

    def getByCourse(self,c_identif):
        self.CourseWeeks.getByCourse(c_identif)

    def exit(self):
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
            with open(normpath(self.courses_directory + course.name + ".html")) as file:
                file.write( page(weeks) )
            course_page_location.append(normpath(self.courses_directory + course.name + ".html"))
        with open(normpath(self.courses_directory+"all_courses.html")) as file:
            file.write(page(course_page_location))


