from src.app.utils.collect_data import CollectData
from src.app import institution

new_students = CollectData().new_students()

if __name__ == "__main__":
    institution.create_user(students=new_students)
