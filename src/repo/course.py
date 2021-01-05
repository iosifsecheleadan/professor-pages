from src.domain.data.course import Course
from src.repo.repository import FileRepositoryInterface


class CourseRepository(FileRepositoryInterface):
    def __init__(self):
        self.courses = []
        self.read_all()
        pass

    def read_all(self):
        pass

    def save_all(self):
        pass

    def create(self, value: Course):
        pass

    def update(self, value: Course):
        pass

    def delete(self, value: Course):
        pass
