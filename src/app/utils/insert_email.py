from unicodedata import normalize

from src.app.utils.create_email_body import create_email
from src.resources.resources_sophia import get_student, put_student


def insert_email_in_sophia(
    id: str,
    rm: str,
    name: str,
    domain: str
) -> None:

    student = get_student.get_student_in_sophia(id=id)

    normalize_name = normalize("NFKD", name).encode("ASCII", "ignore").decode("ASCII")  # noqa: E501
    splite_normalize_name = normalize_name.split(" ")
    first_name = splite_normalize_name[0]

    email = create_email(
        name=first_name,
        rm=rm,
        domain=domain
    )

    contacts = student.get("contatos")

    for contact in contacts:
        if contact["tipoContato"] == 4:
            contact["contato"] = email

            put_student.put_data_student_in_sophia_manager(
                id=id, data=student
            )
