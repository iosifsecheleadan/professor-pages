from sys import exit

from src.ctrl.course import CourseController
from src.ctrl.general import GeneralController
from src.domain.data.announcement import Type
from src.domain.data.course import Course
from src.domain.data.factory import DataFactory

"""
new professor -> prompt
update professor -> prompt
delete professor -> prompt

new about -> prompt
update about -> prompt
delete about -> prompt

new announcement -> prompt
update announcement -> prompt (get by title)
delete announcement -> prompt

new course -> prompt
update course -> prompt (get by name, get by code)
delete course -> prompt
    
new course_week -> prompt
update course_week -> prompt ((get by name, get by code), get by week)
delete course_week -> prompt


new -> prof / about / ann / course / course_week
update -> prof / about / ann / course / course_week
delete -> prof / about / ann / course / course_week


new
upd
del
sel
save
exit

pf
ab
an
co
cw
"""


class InputError(Exception):
    pass


class UserInterface:
    def __init__(self):
        self.General = GeneralController()
        self.Course = CourseController()

    def run(self):
        entity = {  # (list of attributes)
            "new": self.new,

            "update": self.update,
            "upd": self.update,

            "delete": self.delete,
            "del": self.delete,

            "print": self.print,
            "pt": self.print
        }

        general = {
            "save": self.save,
            "help": self.help,
            "exit": self.exit,
        }

        self.start_message()
        while True:
            line = input(">").split(" ")
            if line[0] in general:
                general[line[0]]()
            else:
                try:
                    entity[line[0]](line[1])
                except Exception as e:
                    print(f"Error : {e}")

    def new(self, argument: str):
        commands = {
            "professor": self.new_professor,
            "pf": self.new_professor,

            "about": self.new_about,
            "ab": self.new_about,

            "announcement": self.new_announcement,
            "an": self.new_announcement,

            "course": self.new_course,
            "co": self.new_course,

            "course_week": self.new_course_week,
            "cw": self.new_course_week,
        }

        commands[argument]()

    def new_professor(self):
        professor = DataFactory.basic_professor()
        professor.full_name = input("Full name >")
        professor.title = input("Title >")
        professor.personal_email = input("Personal Email >")
        professor.faculty_email = input("Faculty Email >")
        professor.office_hours_timeframe = input("Office Hours Timeframe >")
        professor.office_hours_location = input("Office Hours Location >")
        professor.profile_img = input_document_location("Profile Image Location >")
        professor.additional_info = input_document_location("Additional Info Document Location >")
        self.General.create_professor(professor)

    def new_about(self):
        about = DataFactory.basic_about()
        about.documents = input_document_list("Document Location >")
        self.General.create_about(about)

    def new_announcement(self):
        announcement = DataFactory.basic_announcement()
        announcement.title = input("Title >")
        announcement.document = input_document_location("Document Location >")
        announcement.type = input_announcement_type()
        self.General.add_announcement(announcement)

    def new_course(self):
        course = DataFactory.basic_course()
        course.name = input("Name >")
        course.code = input("Code >")
        course.faculty = input("Faculty >")
        course.study_year = input_int("Study Year >")
        course.no_weeks = input_int("Number of Weeks >")
        self.Course.add_course(course)

    def new_course_week(self):
        course_week = DataFactory.basic_course_week()
        course = self.get_course()
        course_week.week_number = input_int("Week Number >")
        course_week.documents = input_document_list("Document Location >")
        self.Course.add_course_week(course_week, course)

    def get_course(self, name_or_code=None) -> Course:
        if name_or_code is None:
            name_or_code = input("Course name or code >")
        while True:
            if name_or_code == "exit": return
            value = self.Course.get_by_name(name_or_code)
            if value is None:
                value = self.Course.get_by_code(name_or_code)
                if value is not None: return value
                else: print("Error : Course with given Name or Code doesn't exist")
            name_or_code = input("Course name or code >")

    def update(self, argument: str):
        commands = {
            "professor": self.update_professor,
            "pf": self.update_professor,

            "about": self.update_about,
            "ab": self.update_about,

            "announcement": self.update_announcement,
            "an": self.update_announcement,

            "course": self.update_course,
            "co": self.update_course,

            "course_week": self.update_course_week,
            "cw": self.update_course_week,
        }

        commands[argument]()

    def update_professor(self):
        professor = self.General.get_professor()
        professor.full_name = input_or_same("Full name >", professor.full_name)
        professor.title = input_or_same("Title >", professor.title)
        professor.personal_email = input_or_same("Personal Email >", professor.personal_email)
        professor.faculty_email = input_or_same("Faculty Email >", professor.faculty_email)
        professor.office_hours_timeframe = input_or_same("Office Hours Timeframe >", professor.office_hours_timeframe)
        professor.office_hours_location = input_or_same("Office Hours Location >", professor.office_hours_location)
        professor.profile_img = input_document_location_or_same("Profile Image Location >",
                                                                professor.profile_img.location)
        professor.additional_info = input_document_location_or_same("Additional Info Document Location >",
                                                                    professor.additional_info.location)
        self.General.update_professor(professor)

    def update_about(self):
        about = self.General.get_about()
        about.documents = input_document_list_or_same("About Document Location >", about.documents)
        self.General.update_about(about)

    def update_announcement(self):
        announcement = self.General.get_by_title(input("Announcement Title >"))
        announcement.title = input("Title >")
        announcement.document = input_document_location_or_same("Document Location >", announcement.document.location)
        announcement.type = input_announcement_type_or_same(announcement.type)
        self.General.update_announcement(announcement)

    def update_course(self):
        course = self.get_course()
        course.name = input_or_same("Name >", course.name)
        course.code = input_or_same("Code >", course.code)
        course.faculty = input_or_same("Faculty >", course.faculty)
        course.study_year = input_int_or_same("Study Year >", course.study_year)
        course.no_weeks = input_int_or_same("Number of Weeks >", course.no_weeks)
        self.Course.update_course(course)

    def update_course_week(self):
        course = self.get_course()
        week = input_int("Course Week Number >")
        course_week = self.Course.get_by_week(course.get_id(), week)
        course_week.week_number = input_int_or_same("Week Number >", course_week.week_number)
        course_week.documents = input_document_list_or_same("Document Location >", course_week.documents)
        self.Course.update_course_week(course_week)

    def delete(self, argument: str):
        commands = {
            "professor": self.delete_professor,
            "pf": self.delete_professor,

            "about": self.delete_about,
            "ab": self.delete_about,

            "announcement": self.delete_announcement,
            "an": self.delete_announcement,

            "course": self.delete_course,
            "co": self.delete_course,

            "course_week": self.delete_course_week,
            "cw": self.delete_course_week,
        }

        commands[argument]()

    def delete_professor(self):
        if are_you_sure(): self.General.delete_professor()

    def delete_about(self):
        if are_you_sure(): self.General.delete_about()

    def delete_announcement(self):
        announcement = self.General.get_by_title(input("Announcement Title >"))
        print(announcement)
        if are_you_sure(): self.General.remove_announcement(announcement)

    def delete_course(self):
        course = self.get_course()
        print(course)
        if are_you_sure(): self.Course.remove_course(course)

    def delete_course_week(self):
        course = self.get_course()
        week = input_int("Course Week Number >")
        course_week = self.Course.get_by_week(course.get_id(), week)
        if are_you_sure(): self.Course.remove_course_week(course_week)

    def print(self, argument: str):
        commands = {
            "professor": self.print_professor,
            "pf": self.print_professor,

            "about": self.print_about,
            "ab": self.print_about,

            "announcement": self.print_announcement,
            "an": self.print_announcement,

            "course": self.print_course,
            "co": self.print_course,

            "course_week": self.print_course_week,
            "cw": self.print_course_week,
        }

        commands[argument]()

    def print_professor(self):
        print(self.General.get_professor())

    def print_about(self):
        print(self.General.get_about())

    def print_announcement(self):
        title = input("Announcement Title >")
        if title != "all":
            print(self.General.get_by_title(title))
            return
        for announcement in self.General.Announcements.announcements:
            print(announcement)

    def print_course(self):
        name_or_code = input("Course name or code >")
        if name_or_code == "all":
            for name_or_code in self.Course.Courses.courses:
                print(name_or_code)
            return
        name_or_code = self.get_course(name_or_code)
        if name_or_code is None: return
        print(name_or_code)
        if not are_you_sure("Print course weeks? >"): return
        for course_week in self.Course.get_by_course(name_or_code.get_id()):
            print(course_week)

    def print_course_week(self):
        course = self.get_course()
        week = input_int("Course Week Number >")
        print(self.Course.get_by_week(course.get_id(), week))

    def save(self):
        self.General.save()
        self.Course.save()

    def exit(self):
        self.save()
        exit()

    def help(self):
        print("""
    Professor Pages

    Create HTML web pages destined to professors, using a command line interface.

    -   Create new entity
        new [professor | about | announcement | course | course_week]
    
    -   Update existing entity
        update [professor | about | announcement | course | course_week]
    
    -   Delete existing entity
        delete [professor | about | announcement | course | course_week]
    
    -   Print existing entity
        print [professor | about | announcement | course | course_week]
    
    -   Display this message
        help
    
    -   Save
        save
    
    -   Save and Exit
        exit
    
    -   Just Exit
        Ctrl + C

    -   Abbreviations:
        [update | delete | print | professor | about | announcement | course | course_week]
        [upd    | del    | pt    | pf        | ab    | an           | co     | cw         ]
        """)

    def start_message(self):
        print("""
Professor Pages

Loading data ...

(type help for help)
""")


def are_you_sure(message: str = "Are you sure? >"):
    while True:
        value = input(message)
        if value in ["n", "N", "no", "No", "NO"]:
            return False
        elif value in ["y", "Y", "yes", "Yes", "YES"]:
            return True
        print("Answer must be yes or no. Please try again.")


def input_int(message: str):
    while True:
        try:
            return int(input(message))
        except Exception as e:
            print(f"Error : {e} \nPlease try again")


def input_announcement_type():
    while True:
        a_type = input("Type >")
        if a_type in ["normal", "nm", "0"]:
            return Type.NORMAL
        elif a_type in ["important", "ip", "1"]:
            return Type.IMPORTANT
        elif a_type in ["very important", "vi", "2"]:
            return Type.VERY_IMPORTANT
        else:
            print("Wrong Input. Please Try again")


def input_document_location(message: str):
    while True:
        try:
            return DataFactory.document_from_csv(input(message))
        except Exception as e:
            print(f"Error : {e} \nPlease try again")


def input_document_list(message: str):
    documents = []
    while True:
        new_document = input(message)
        if new_document == "exit": break
        try:
            documents.append(
                DataFactory.document_from_csv(new_document))
        except Exception as e:
            print(f"Error : {e}")
    return documents


def input_or_same(message: str, old: str):
    print(f"Current {message} : {old}")
    value = input(message)
    if value == "same":
        return old
    else:
        return value


def input_int_or_same(message: str, old: int):
    print(f"Current {message} : {old}")
    while True:
        value = input(message)
        if value == "same": return old
        try:
            return int(input(message))
        except Exception as e:
            print(f"Error : {e} \nPlease try again")


def input_announcement_type_or_same(old: Type):
    print(f"Current Type : {old.name.title()}")
    while True:
        a_type = input("Type >")
        if a_type == "same":
            return old
        elif a_type in ["normal", "nm", "0"]:
            return Type.NORMAL
        elif a_type in ["important", "ip", "1"]:
            return Type.IMPORTANT
        elif a_type in ["very important", "vi", "2"]:
            return Type.VERY_IMPORTANT
        else:
            print("Wrong Input. Please Try again")


def input_document_location_or_same(message: str, old: str):
    print(f"Current {message} : {old}")
    while True:
        try:
            value = input(message)
            if value == "same":
                return DataFactory.document_from_csv(old)
            else:
                return DataFactory.document_from_csv(value)
        except Exception as e:
            print(f"Error : {e} \nPlease try again")


def input_document_list_or_same(message: str, documents: list):
    new_documents = []
    for document in documents:
        print(f"Current {message} : {document.location}")
        try:
            value = input(message)
            if value == "same":
                new_documents.append(DataFactory.document_from_csv(document.location))
            elif value in ["del", "delete"]:
                pass
            else:
                new_documents.append(DataFactory.document_from_csv(value))
        except Exception as e:
            print(f"Error : {e} \nPlease try again")
    print("Add new documents:")
    new_documents.extend(input_document_list(message))
    return new_documents
