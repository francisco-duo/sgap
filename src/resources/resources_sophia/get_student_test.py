from .get_student import get_student_in_sophia
from config import settings


def test_url_to_get_student_by_id(id="996"):
    url = settings.GET_STUDENT + id

    assert url == "https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos/996"


def test_getting_student_in_sophia():
    request = get_student_in_sophia(id="996")

    assert type(request) == dict
