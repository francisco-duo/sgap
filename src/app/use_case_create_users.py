from src.app.utils.collect_data import CollectData
from src.app import institution

from src.resources.resources_sophia import get_classroom

new_students = CollectData().new_students()
students = CollectData().all_students()
classrooms = get_classroom.get_classroom_of_sophia()

if __name__ == "__main__":
    institution.create_user(students=new_students)
    institution.create_group(groups=classrooms)
    institution.insert_user_in_group(students=students)
