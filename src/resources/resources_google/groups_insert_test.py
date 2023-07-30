import pytest

from src.app.utils.return_classroom import return_classroom_dict
from .groups_insert import insert_group_in_admin


@pytest.mark.skip(reason="sensive test")
def test_insert_group():
    body = return_classroom_dict(
        domain="faculdadecci.com.br",
        name="KIKO",
        period="2023"
    )

    insert_group_in_admin(body=body)
