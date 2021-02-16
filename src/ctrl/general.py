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
        self.AboutProfessor.create_professor(professor)

    def update_professor(self, professor: Professor):
        self.AboutProfessor.update_professor(professor)

    def create_about(self, about: About):
        self.AboutProfessor.create_about(about)

    def update_about(self, about: About):
        self.AboutProfessor.update_about(about)

    def add_announcement(self, announcement: Announcement):
        self.Announcements.create(announcement)

    def update_announcement(self, announcement: Announcement):
        self.Announcements.update(announcement)

    def remove_announcement(self, announcement: Announcement):
        self.Announcements.delete(announcement)

    def get_by_title(self, title: str):
        return self.Announcements.getByTitle(title)

    def save(self):
        self.AboutProfessor.save_all()
        self.Announcements.save_all()
        self._create_pages()

    def _create_pages(self):
        html_pageAnn = page(self.Announcements.announcements)
        with open(self.announcements_page_location, "w") as file1:
            file1.write(html_pageAnn)

        html_pageHome = page([self.AboutProfessor.professor])
        with open(self.professor_page_location, "w") as file2:
            file2.write(html_pageHome)
        html_pageAbout = page([self.AboutProfessor.about])
        with open(self.about_page_location, "w") as file3:
            file3.write(html_pageAbout)

    def get_professor(self):
        return self.AboutProfessor.professor

    def get_about(self):
        return self.AboutProfessor.about

    def delete_professor(self):
        self.AboutProfessor.delete_professor()

    def delete_about(self):
        self.AboutProfessor.delete_about()


