import requests

from src.connections import sophia
from config import settings


def put_data_student_in_sophia_manager(id: str, data: object) -> dict:
    return requests.put(settings.PUT_STUDENTS + id, json=data, headers=sophia)
