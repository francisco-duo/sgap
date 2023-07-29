from .return_domain import return_the_domain
from src.app.utils.collect_data import CollectData

new_students = CollectData().all_students()


def test_if_the_function_return_a_domain():
    for students in new_students:
        mock_domain = return_the_domain(students=students["classroom"])
        print(mock_domain)
