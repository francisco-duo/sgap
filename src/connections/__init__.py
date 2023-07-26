from .connection_google import connect_to_admin_sdk
from .connection_sophia import connect_to_sophia

service = connect_to_admin_sdk()
sophia = connect_to_sophia()
