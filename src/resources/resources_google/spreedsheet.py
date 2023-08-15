from datetime import datetime

from src.connections import spreadsheet
from config import settings

spreadsheet_id = settings.SPREADSHEET_ID


def member_log(email: str, group_email: str, action, tab):
    sheet_name = tab
    range_name = f'{sheet_name}!A:D'

    log_data = [[datetime.now().strftime('%d/%m/%Y %H:%M:%S'), email, group_email, action]]

    body = {'values': log_data}

    spreadsheet.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='USER_ENTERED', body=body
    ).execute()


def read_spreadsheet(tab: str) -> list:
    sheet_name = tab
    range_name = f"{sheet_name}!A:B"

    result = spreadsheet.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name,
    ).execute()

    rows = result.get("values", [])

    return rows


if __name__ == "__main__":
    sheet = read_spreadsheet("email dos grupos tec")

    for data in sheet:
        print(data[1])
