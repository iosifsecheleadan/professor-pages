from src.domain.data.course_week import CourseWeek
from src.repo.repository import FileRepositoryInterface


class CourseWeekRepository(FileRepositoryInterface):
    def __init__(self):
        self.weeks = []
        self.read_all()
        pass

    def read_all(self):
        pass

    def save_all(self):
        pass

    def create(self, value: CourseWeek):
        pass

    def update(self, value: CourseWeek):
        pass

    def delete(self, value: CourseWeek):
        pass
    def getByWeek(self,c_identif,week_nr):
        pass