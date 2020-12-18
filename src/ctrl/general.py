from src.ctrl.controller import WebControllerInterface
from src.domain.data.about import About
from src.domain.data.announcement import Announcement
from src.domain.data.professor import Professor
from src.repo.about_professor import AboutProfessorRepository
from src.repo.announcement import AnnouncementRepository


class GeneralController(WebControllerInterface):
    def __init__(self):
        self.AboutProfessor = AboutProfessorRepository()
        self.Announcements = AnnouncementRepository()

    def create_professor(self, professor: Professor):
        pass

    def update_professor(self, professor: Professor):
        pass

    def create_about(self, about: About):
        pass

    def update_about(self, about: About):
        pass

    def add_announcement(self, announcement: Announcement):
        pass

    def update_announcement(self, announcement: Announcement):
        pass

    def remove_announcement(self, announcement: Announcement):
        pass

    def exit(self):
        self.AboutProfessor.save_all()
        self.Announcements.save_all()
        self._create_pages()

    def _create_pages(self):
        pass



