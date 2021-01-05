from src.domain.data.announcement import Announcement
from src.domain.data.factory import DataFactory
from src.repo.repository import FileRepositoryInterface
from os.path import normpath

class AnnouncementRepository(FileRepositoryInterface):
    def __init__(self):
        self.__file_location = normpath("../resources/announcements.txt")
        self.announcements = []
        self.__lastId = 0
        self.read_all()

    def read_all(self):
        with open(self.__file_location, "r") as file:
            for line in file.readlines():
                new = DataFactory.announcement_from_csv(line)
                self.__lastId = new.get_id()
                self.announcements.append( new )
        self.__lastId += 1

    def save_all(self):
        with open(self.__file_location, "w") as file:
            for announcement in self.announcements:
                file.write(announcement.to_csv() + "\n")

    def create(self, value: Announcement):
        value.set_id(self.__lastId)
        self.__lastId += 1
        self.announcements.append(value)

    def update(self, value: Announcement):
        for announcement in self.announcements:
            if announcement == value:
                value.set_id(announcement.get_id())
                self.announcements.remove(announcement)
                self.announcements.append(value)

    def delete(self, value: Announcement):
        self.announcements.remove(value)
        pass

    def getByTitle(self,title):
        pass


