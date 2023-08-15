import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

from config import settings

try:
    creds = service_account.Credentials.from_service_account_file(
        filename=settings.PATH_CREDENTIALS,
        scopes=list(settings.SCOPES),
        subject=settings.SERVICE_ACCOUNT
    )

except Exception as e:
    if os.path.exists(settings.PATH_CREDENTIALS):
        raise Exception(
            f"The file exists. Verify your connection to google api.\n{e}"
        )
    else:
        raise Exception(
            f"The crendential.json is not exist.\n{e}"
        )


def connect_to_admin_sdk() -> build:
    return build('admin', 'directory_v1', credentials=creds)


def connect_to_spreadsheets() -> build:
    return build('sheets', 'v4', credentials=creds)


if __name__ == "__main__":
    connect_to_admin_sdk()
