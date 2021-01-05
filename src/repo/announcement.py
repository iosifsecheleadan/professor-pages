from src.domain.data.announcement import Announcement
from src.repo.repository import FileRepositoryInterface


class AnnouncementRepository(FileRepositoryInterface):
    def __init__(self):
        self.read_all()
        pass

    def read_all(self):
        pass

    def save_all(self):
        pass

    def create(self, value: Announcement):
        pass

    def update(self, value: Announcement):
        pass

    def delete(self, value: Announcement):
        pass
    def getByTitle(self,title):
        pass
