from os.path import normpath

from src.domain.data.about import About
from src.domain.data.professor import Professor
from src.repo.repository import FileRepositoryInterface


class AboutProfessorRepository(FileRepositoryInterface):
    def __init__(self):
        self.read_all()
        self.about = None
        self.professor = None
        self.about_file_location = normpath("../../resources/about.txt")
        self.professor_file_location = normpath("")
        pass

    def read_all(self):
        pass

    def save_all(self):
        pass

    def create_professor(self, value: Professor):
        pass

    def update_professor(self, value: Professor):
        pass

    def create_about(self, value: About):
        pass

    def update_about(self, value: About):
        pass

