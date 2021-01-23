from src.domain.data.course_week import CourseWeek
from src.domain.data.factory import DataFactory
from src.repo.repository import FileRepositoryInterface
from os.path import normpath


class CourseWeekRepository(FileRepositoryInterface):
    def __init__(self):
        self.__weeks_file_location = normpath("../resources/week.txt")
        self.__weekLastId = 0
        self.weeks = []
        self.read_all()



    def read_all(self):
        with open(self.__weeks_file_location, "r") as file:
            for line in file.readlines():
                new = DataFactory.course_from_csv(line)
                self.__weekLastId = new.get_id()
                self.weeks.append(new)
        self.__weekLastId += 1

    def save_all(self):
        with open(self.__weeks_file_location,"w") as file:
            for week in self.weeks:
                file.write(week.to_csv()+"\n")

    def create(self, value: CourseWeek):
        value.set_id(self.__weekLastId)
        self.__weekLastId += 1
        self.weeks.append(value)

    def update(self, value: CourseWeek):
        for week in self.weeks:
            if week == value:
                value.set_id(week.get_id())
                self.weeks.remove(week)
                self.weeks.append(value)

    def delete(self, value: CourseWeek):
        self.weeks.remove(value)

    def getByWeek(self,c_identif,week_nr):
        for week in self.weeks:
            if week.week_number == week_nr and week.course_identifier==c_identif:
                return week

    def getByCourse(self,c_identif):
        vectCourse=[]
        for week in self.weeks:
            if c_identif == week.course_identifier:
                vectCourse.appent(week)
        return vectCourse