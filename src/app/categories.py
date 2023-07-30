from .institution import Institution

from src.app.utils.insert_email import insert_email_in_sophia
from src.app.utils.return_domain import return_the_domain
from src.app.utils.return_classroom import return_classroom_dict

from src.resources.resources_google import groups_insert, members_insert


class Institutions(Institution):

    def create_user(self, students: list):
        for s in students:
            id = s['id']
            rm = s['rm']
            name = s['name']

            domain = return_the_domain(students=s["classroom"])

            insert_email_in_sophia(
                id=id,
                rm=rm,
                name=name,
                domain=domain
            )

    def create_group(self, groups: list):
        for group in groups:
            domain = return_the_domain(students=group["nome"])

            body = return_classroom_dict(
                domain=domain, name=group["nome"]
            )

            groups_insert.insert_group_in_admin(body=body)

    def insert_user_in_group(self, students: list):
        for s in students:
            domain = return_the_domain(students=s["classroom"])

            group = return_classroom_dict(
                domain=domain, name=s["classroom"]
            )

            members_insert.insert_member_in_group(
                group=group["email"], email=s["email"], role="MEMBER"
            )
