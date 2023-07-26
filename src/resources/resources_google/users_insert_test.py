import pytest

from .users_insert import insert_user_in_admin_sdk


@pytest.mark.skip(reason="Sensive test")
def test_if_function_insert_a_user_in_google_sdk():
    insert_user_in_admin_sdk(
        domain="cciweb.com.br",
        name="onzestecnologia teste da silva",
        rm="11111"
    )
