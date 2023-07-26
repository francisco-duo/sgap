from .users_list import list_all_users_of_admin_sdk


def test_checking_if_function_return_a_list():
    user_list = list_all_users_of_admin_sdk('faculdadecci.com.br')

    assert type(user_list) == list
