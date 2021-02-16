from src.domain.data.course import Course
from src.repo.repository import FileRepositoryInterface
from src.domain.data.factory import DataFactory
from os.path import normpath


class CourseRepository(FileRepositoryInterface):
    def __init__(self):
        self.__course_file_location = normpath("../resources/course.txt")
        self.courses = []
        self.__courseLastId = 0
        self.read_all()


    def read_all(self):
        with open(self.__course_file_location, "r") as file:
            for line in file.readlines():
                new = DataFactory.course_from_csv(line)
                self.__courseLastId = new.get_id()
                self.courses.append(new)
        self.__courseLastId += 1

    def save_all(self):
        with open(self.__course_file_location,"w") as file:
            for course in self.courses:
                file.write(course.to_csv()+"\n")

    def create(self, value: Course):
        value.set_id(self.__courseLastId)
        self.__courseLastId += 1
        self.courses.append(value)

    def update(self, value: Course):
        for course in self.courses:
            if course == value:
                value.set_id(course.get_id())
                self.courses.remove(course)
                self.courses.append(value)

    def delete(self, value: Course):
        self.courses.remove(value)

    def getByName(self,name):
        for course in self.courses:
            if course.name == name:
                return course
        return None

    def getByCode(self,code):
        for course in self.courses:
            if course.code == code:
                return  course
        return None