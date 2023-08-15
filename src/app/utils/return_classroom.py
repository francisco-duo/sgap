from unicodedata import normalize


def return_classroom_dict(domain: str, name: str) -> dict:
    match domain:
        case "cciweb.com.br":
            period = "2023"
            name_group = name\
                .replace(" ", "")\
                .replace("ª", "")\
                .replace("º", "")\
                .replace("°", "")\
                .split("-")

            normalize_name = normalize('NFKD', name_group[0])\
                .encode('ASCII', 'ignore').decode('ASCII')

            return {
                "name": f"{name_group[0]} - {period}",
                "email": f"{normalize_name}_{period}@{domain}".lower()
            }

        case "tecscci.com.br":
            period = "2023.2"
            name_group = name\
                .replace(" ", "")\
                .replace("ª", "")\
                .replace("º", "")\
                .replace("°", "")\
                .replace(".", "")\
                .replace("-", "")

            normalize_name = normalize('NFKD', name_group)\
                .encode('ASCII', 'ignore').decode('ASCII')

            return {
                "name": f"{name_group} {period}",
                "email": f"{normalize_name}_{period}@{domain}".lower()
            }
        case "faculdadecci.com.br":
            period = "2023.2"

            return {
                "name": f"{name} - {period}",
                "email": f"{name}_{period}@{domain}".lower()
            }
