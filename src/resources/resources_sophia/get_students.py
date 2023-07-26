import requests

from src.connections import sophia
from config import settings


def get_students_of_sophia() -> list:
    return requests.get(
        settings.GET_STUDENTS, headers=sophia
    ).json()
