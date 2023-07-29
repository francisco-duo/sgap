from .institution import Institution

from src.app.utils.collect_data import CollectData
from src.app.utils.insert_email import insert_email_in_sophia
from src.app.utils.return_domain import return_the_domain

from src.resources.resources_sophia import get_classroom

SUP_PERIOD = "2023.2"
BASIS_PERIOD = "2023"

new_students = CollectData().new_students()
students = CollectData().all_students()
classrooms = get_classroom.get_classroom_of_sophia()


class Institutions(Institution):

    def create_user(self, ):
        for students in new_students:
            domain = return_the_domain(students=students["classroom"])

            id = students['id']
            rm = students['rm']
            name = students['name']

            insert_email_in_sophia(
                id=id,
                rm=rm,
                name=name,
                domain=domain
            )


class BasicEducation(Institution):

    def create_group(self, ): pass

    def insert_user_in_group(self, ): pass

    def remove_of_group(self, ): pass


class TechnicalEducation(Institution):

    def create_group(self, ): pass

    def insert_user_in_group(self, ): pass

    def remove_of_group(self, ): pass


class SuperiorEducation(Institution):

    def create_group(self, ): pass

    def insert_user_in_group(self, ): pass

    def remove_of_group(self, ): pass
