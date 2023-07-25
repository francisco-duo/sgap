import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

from config.dynaconf_config import settings


def connect_to_admin_sdk() -> build:
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

    return build('admin', 'directory_v1', credentials=creds)
