from .connection_google import connect_to_admin_sdk, connect_to_spreadsheets
from .connection_sophia import connect_to_sophia

service = connect_to_admin_sdk()
spreadsheet = connect_to_spreadsheets()
sophia = connect_to_sophia()
