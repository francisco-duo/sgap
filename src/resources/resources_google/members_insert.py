from src.connections import service
from .spreedsheet import member_log
from googleapiclient.errors import HttpError


def insert_member_in_group(group: str, email: str, role: str):
    body = {
        "email": email,
        "role": role
    }

    try:
        service.members().insert(
            body=body,
            groupKey=group
        ).execute()

    except HttpError as e:
        pass
