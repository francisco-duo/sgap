from .return_classroom import return_classroom_dict

case_01 = return_classroom_dict(
    domain="cciweb.com.br",
    name="Maternal 1ºA - Tia Eysla",
    period="2023"
)
case_02 = return_classroom_dict(
    domain="tecscci.com.br",
    name="Téc.Enf1ºM - A",
    period="2023.2"
)
case_03 = return_classroom_dict(
    domain="faculdadecci.com.br",
    name="ADS03",
    period="2023.2"
)


def test_checking_if_function_return_a_dict():

    assert type(case_01) == dict
    assert type(case_02) == dict
    assert type(case_03) == dict


def test_checkin_return_of_function():
    print(case_01)
    print(case_02)
    print(case_03)
