from src.connections import service


def insert_member_in_group(group: str, email: str, role: str):
    body = {
        "email": email,
        "role": role
    }

    service.members().insert(
        body=body,
        groupKey=group
    )
