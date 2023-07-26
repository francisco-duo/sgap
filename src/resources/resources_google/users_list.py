from src.connections import service


def list_all_users_of_admin_sdk(domain: str) -> list:
    set_of_users = []
    page_token = None

    while True:
        response = service.users().list(
            domain=domain,
            pageToken=page_token
        ).execute()

        page_token = response.get("nextPageToken", None)

        for user in response["users"]:

            try:
                set_of_users.append(user)
            except Exception as e:
                raise Exception(
                    f"Error:\
                        Maybe the user object don't exist or you missed one\
                            requiriment argument\n{e}"
                )

        if not page_token:
            break

    return set_of_users
