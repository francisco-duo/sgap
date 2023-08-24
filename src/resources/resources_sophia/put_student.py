import requests

from src.connections import sophia
from config import settings


def put_data_student_in_sophia_manager(id: str, data: dict) -> dict:
    return requests.put(settings.PUT_STUDENTS + str(id), json=data, headers=sophia)
