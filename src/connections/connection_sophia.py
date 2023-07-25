import requests

from config.dynaconf_config import settings


def connect_to_sophia():
    access_key = {
        "token": requests.post(
            settings.POST_AUTH, json=settings.SOPHIA_ACCESS
        ).text
    }

    return access_key
