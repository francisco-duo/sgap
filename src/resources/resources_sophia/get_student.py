import requests

from src.connections import sophia
from config import settings


def get_student_in_sophia(id: str) -> dict:
    return requests.get(settings.GET_STUDENT + str(id), headers=sophia).json()
