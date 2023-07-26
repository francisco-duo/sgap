import requests

from src.connections import sophia
from config import settings


def get_classroom_of_sophia() -> list:
    return requests.get(settings.GET_CLASSROOM, headers=sophia).json()
