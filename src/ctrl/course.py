from src.ctrl.controller import WebControllerInterface
from src.domain.data.course import Course
from src.domain.data.course_week import CourseWeek
from src.repo.course import CourseRepository
from src.repo.course_week import CourseWeekRepository


class CourseController(WebControllerInterface):
    def __init__(self):
        self.Courses = CourseRepository()
        self.CourseWeeks = CourseWeekRepository()

    def add_course(self, course: Course):
        pass

    def update_course(self, course: Course):
        pass

    def remove_course(self, course: Course):
        pass

    def add_course_week(self, course_week: CourseWeek):
        pass

    def update_course_week(self, course_week: CourseWeek):
        pass

    def remove_course_week(self, course_week: CourseWeek):
        pass

    def getByName(self,name):
        pass
    def getByCode(self,code):
        pass

    def getByWeek(self, c_identif, week_nr):
        pass

    def exit(self):
        self.Courses.save_all()
        self.CourseWeeks.save_all()
        self._create_pages()

    def _create_pages(self):
        pass


