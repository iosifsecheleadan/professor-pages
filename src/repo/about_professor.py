from os.path import normpath
from src.domain.data.factory import DataFactory
from src.domain.data.about import About
from src.domain.data.professor import Professor
from src.repo.repository import FileRepositoryInterface
from src.domain.data.base import DataException

class AboutProfessorRepository(FileRepositoryInterface):
    def __init__(self):
        self.about = None
        self.professor = None
        self.__about_file_location = normpath("../resources/about.txt")
        self.__professor_file_location = normpath("../resources/professor.txt")
        self.read_all()

    def read_all(self):
        with open(self.__professor_file_location, "r") as file1:
            try:
                line1 = file1.readline()
                new1 = DataFactory.professor_from_csv(line1)
                self.professor = new1
            except DataException as e:
                pass

        with open(self.__about_file_location, "r") as file2:
            try:
                line2 = file2.readline()
                new2 = DataFactory.about_from_csv(line2)
                self.about = new2
            except DataException as e :
                pass

    def save_all(self):
        with open(self.__professor_file_location, "w") as file:
            if self.professor is not None:
                 file.write(self.professor.to_csv() + "\n")
        with open(self.__about_file_location, "w") as file2:
            if self.about is not  None:
                file2.write(self.about.to_csv() + "\n")

    def create_professor(self, value: Professor):
        self.professor = value

    def update_professor(self, value: Professor):
        if self.professor == value:
            self.professor = value

    def create_about(self, value: About):
        self.about = value

    def update_about(self, value: About):
        if self.about == value:
            self.about = value
