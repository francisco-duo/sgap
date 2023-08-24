import time

from src.app.utils.insert_email import insert_email_in_sophia
from src.app.utils.return_domain import return_the_domain
from src.app.utils.return_classroom import return_classroom_dict

from src.resources.resources_google import groups_insert, members_insert, users_insert, spreedsheet

from googleapiclient.errors import HttpError


class Institutions:

    @staticmethod
    def create_user(students: list, ):
        for s in students:
            time.sleep(0.5)
            id = s['id']
            rm = s['rm']
            name = s['name']

            first_name = name.split(" ")[-1]

            domain = return_the_domain(students=s["classroom"])
            try:
                users_insert.insert_user_in_admin_sdk(
                    domain=domain,
                    name=name,
                    rm=rm
                )
            except Exception:
                pass

            insert_email_in_sophia(
                id=id,
                rm=rm,
                name=name,
                domain=domain
            )

            spreedsheet.member_log(
                email=name, group_email=f"{first_name}{rm}@{domain}", action="CREATE", tab="emails"
            )

    @staticmethod
    def create_group(groups: list, ):
        for group in groups:
            time.sleep(0.5)
            domain = return_the_domain(students=group["nome"])

            body = return_classroom_dict(
                domain=domain, name=group["nome"]
            )
            try:
                groups_insert.insert_group_in_admin(body=body)

                spreedsheet.member_log(
                    email=body["name"], group_email=body["email"], action="CREATE", tab="grupos"
                )
            except HttpError as e:
                spreedsheet.member_log(
                    email=body["name"], group_email=body["email"], action=e, tab="grupos"
                )

    @staticmethod
    def insert_user_in_group(students: list, ):
        for s in students:
            time.sleep(0.5)
            try:
                domain = return_the_domain(students=s["classroom"])

                group = return_classroom_dict(
                    domain=domain, name=s["classroom"]
                )

                members_insert.insert_member_in_group(
                    group=group["email"], email=s["email"], role="MEMBER"
                )

                spreedsheet.member_log(
                    email=s["email"], group_email=group["email"], action="INSERT", tab="membros"
                )
            except TypeError as e:
                spreedsheet.member_log(
                    email=s["name"], group_email="None", action=e, tab="membros"
                )


if __name__ == "__main__":
    members_insert.insert_member_in_group(
        group="tecenf1ma_2023.2@tecscci.com.br", email="francisco.duo@portalcci.com.br", role="MEMBER"
    )
