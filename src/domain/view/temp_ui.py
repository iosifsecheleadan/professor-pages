from src.domain.data.base import DataException
from src.domain.data.factory import DataFactory
from src.domain.view.page import page


class TempUI:
    def __init__(self):
        self.file = "temp.html"
        self.objects = [
            DataFactory.professor_from_csv("1,Sechelea Iosif,Professor,iosif@gmail.com,iosif@prof.com,16 - 18,zoom,profile.png,yes.pdf"),
            DataFactory.about_from_csv("1,what.md,yes.html"),
            DataFactory.announcement_from_csv("1,Important,important.docx,1"),
            DataFactory.announcement_from_csv("2,Very important,very.md,2"),
            DataFactory.announcement_from_csv("0,Normal,normal.doc,0"),
            DataFactory.course_from_csv("1,Math,MT123,Math Faculty,2,14"),
            DataFactory.course_week_from_csv("1,1,0,Lab.pdf,Course.ppt,Sem.txt"),
            DataFactory.course_week_from_csv("2,1,1,CourseTitle.pdf,LaboratoryTopic.txt,SeminaryProblem.pdf"),
        ]

    def save(self):
        with open(self.file, "w") as html:
            html.write(page(self.objects))

    def run(self):
        switcher = {
            "prof"  : DataFactory.professor_from_csv,
            "about" : DataFactory.about_from_csv,
            "news"  : DataFactory.announcement_from_csv,
            "course": DataFactory.course_from_csv,
            "week"  : DataFactory.course_week_from_csv,
        }

        while True:
            command = input(">")
            if command == "quit":
                self.save()
                return
            if command not in switcher:
                print("Wrong Command")
                continue
            data = input("data:")
            try: self.objects.append(switcher[command](data))
            except DataException as e: print(e)

