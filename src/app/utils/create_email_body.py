def create_email(
    name: str,
    rm: str,
    domain: str
):
    lower_name = name.lower()

    return f"{lower_name}{rm}@{domain}"
