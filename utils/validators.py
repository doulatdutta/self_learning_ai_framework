import re

def is_valid_email(email):
    """
    Validates if the given email is valid based on a regular expression pattern.

    :param email: The email address to validate.
    :return: True if valid, False otherwise.
    """
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    """
    Validates if the given password meets certain security criteria.

    :param password: The password to validate.
    :return: True if valid, False otherwise.
    """
    return len(password) >= 8 and any(char.isdigit() for char in password)
