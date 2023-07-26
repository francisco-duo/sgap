from src.connections import service
from unicodedata import normalize
from googleapiclient.errors import HttpError


def insert_user_in_admin_sdk(domain: str, name: str, rm: str) -> None:
    body = {
        "name": {
            "familyName": "",
            "givenName": "",
            "fullName": "",
            "displayName": ""
        },
        "password": "",
        "primaryEmail": "",
        "changePasswordAtNextLogin": True
    }

    normalize_name = normalize(
            'NFKD', name
        ).encode('ASCII', 'ignore').decode('ASCII')

    split_normalize_name = normalize_name.split(' ')

    family_name = split_normalize_name[-1]
    given_name = split_normalize_name[0]

    primary_email = f'{given_name}{rm}@{domain}'
    password = f'CCI{rm}'

    body['password'] = password
    body['primaryEmail'] = primary_email.lower()

    user_name_body = body['name']

    user_name_body['familyName'] = family_name
    user_name_body['givenName'] = given_name
    user_name_body['fullName'] = name
    user_name_body['displayName'] = name

    try:
        service.users().insert(
            body=body
        ).execute()

    except HttpError as e:
        raise Exception(f"Error:\
            HttpError verify if a some user info has missed.\n\
                {e}")
