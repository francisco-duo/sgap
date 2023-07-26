from .get_students import get_students_of_sophia


def test_checking_if_get_students_of_sophia_return_a_list():
    request = get_students_of_sophia()

    assert type(request) == list
