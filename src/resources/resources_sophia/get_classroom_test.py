from .get_classroom import get_classroom_of_sophia


def test_checking_the_type_of_request_classroom():
    request = get_classroom_of_sophia()

    assert type(request) == list


def test_checkin_the_name_of_classrooms():
    request = get_classroom_of_sophia()

    for r in request:
        print(r["nome"])
