from .connection_sophia import connect_to_sophia


def test_connection_to_sophia():
    connection = connect_to_sophia()

    assert type(connection) == dict
