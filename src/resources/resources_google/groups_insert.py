from src.connections import service
from googleapiclient.errors import HttpError


def insert_group_in_admin(body: dict):
    try:
        service.groups().insert(
            body=body
        ).execute()
    except HttpError as e:
        return f"Error: The group has be created.\n{e}"
