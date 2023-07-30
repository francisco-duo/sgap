from src.resources.resources_sophia import get_classroom
from src.app import institution

classrooms = get_classroom.get_classroom_of_sophia()

if __name__ == "__main__":
    institution.create_group(groups=classrooms)
