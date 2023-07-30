from src.app.utils.collect_data import CollectData
from src.app import institution

students = CollectData().all_students()

if __name__ == "__main__":
    institution.insert_user_in_group(students=students)
