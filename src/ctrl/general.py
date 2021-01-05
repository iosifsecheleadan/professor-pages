from os.path import normpath

from src.ctrl.controller import WebControllerInterface
from src.domain.data.about import About
from src.domain.data.announcement import Announcement
from src.domain.data.professor import Professor
from src.domain.view.page import page
from src.repo.about_professor import AboutProfessorRepository
from src.repo.announcement import AnnouncementRepository


class GeneralController(WebControllerInterface):
    def __init__(self):
        self.professor_page_location = normpath("../page/home.html")
        self.about_page_location = normpath("../page/about.html")
        self.announcements_page_location = normpath("../page/announcements.html")
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
        self.Announcements.create(announcement)

    def update_announcement(self, announcement: Announcement):
        self.Announcements.update(announcement)

    def remove_announcement(self, announcement: Announcement):
        self.Announcements.delete(announcement)

    def exit(self):
        self.AboutProfessor.save_all()
        self.Announcements.save_all()
        self._create_pages()

    def _create_pages(self):
        html_page = page(self.Announcements.announcements)
        with open(self.announcements_page_location, "w") as file:
            file.write(html_page)




