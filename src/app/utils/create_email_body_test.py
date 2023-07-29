from .create_email_body import create_email


def test_checking_if_a_function_return_a_valid_email():
    email = create_email(name="francisco", rm="12345", domain="cciweb.com.br")

    print(email)
