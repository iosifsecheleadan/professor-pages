from src.ctrl.course import CourseController
from src.ctrl.general import GeneralController


class UserInterface:
    def __init__(self):
        self.General = GeneralController()
        self.Course = CourseController()

    def run(self):
        """
        Read user input
        Call Controller methods
        Should be : Intuitive and Non-repetitive
        :return:
        """
        pass

    def exit(self):
        self.General.exit()
        self.Course.exit()
