from src.ui.user_interface import UserInterface
from src.ctrl.general import *
from src.domain.data.document import Document
from src.domain.data.announcement import Type
if __name__ == '__main__':
    ui = UserInterface()
    ui.run()

    ctrl=GeneralController()
    ctrl.add_announcement(Announcement("Titlu2",Document("nolocation.a"),Type.NORMAL))
    ctrl.create_professor(Professor(1,"ana","pf","prof@","abc","23","ofvd",Document("nolocation.jpg"),Document("abc.d")))

    ctrl.save()

