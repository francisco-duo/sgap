from .connection_google import connect_to_admin_sdk
from . import service


def test_connetion_with_google_api():
    connection = connect_to_admin_sdk()

    assert type(connection) == type(service)
