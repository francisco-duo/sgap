from .connection_google import connect_to_admin_sdk


def test_connetion_with_google_api():
    connection = connect_to_admin_sdk()

    print("=========-=========")
    print(type(connection))
