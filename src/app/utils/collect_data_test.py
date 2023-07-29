from .collect_data import CollectData

students_obj = CollectData()


def test_if_function_collect_a_student_list():
    type(students_obj.new_students()) == list


def test_if_function_has_all_object():
    print(students_obj.new_students())


# def test_if_function_return_all_students():
#     print(students_obj.all_students()[-1])
