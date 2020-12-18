from src.domain.data.about import About
from src.domain.data.professor import Professor
from src.repo.repository import FileRepositoryInterface


class AboutProfessorRepository(FileRepositoryInterface):
    def __init__(self):
        self.read_all()
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

