from .return_domain import return_the_domain
from src.app.utils.collect_data import CollectData
from src.resources.resources_sophia import get_classroom

new_students = CollectData().all_students()
classroom = get_classroom.get_classroom_of_sophia()


def test_if_the_function_return_a_domain():
    for students in classroom:
        mock_domain = return_the_domain(students=students["nome"])
        print(mock_domain)
