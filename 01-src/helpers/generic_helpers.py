import random
import string
import logging as logger


def generate_random_email_and_password(domain=None, email_prefix=None):
    """
    Generate a random email and password for user registration.
    Returns a dict with 'email' and 'password' keys.
    """

    # set default domain and prefix if not provided
    if not domain:
        domain = "supersqa.com"

    if not email_prefix:
        email_prefix = "testuser"

    # generate random lowercase string for the email
    random_email_string_length = 10
    random_string = ''.join(
        random.choices(string.ascii_lowercase, k=random_email_string_length)
    )

    # assemble email address
    email = f"{email_prefix}_{random_string}@{domain}"

    # generate a random password (letters only for now)
    rand_password_length = 20
    rand_password = ''.join(
        random.choices(string.ascii_letters, k=rand_password_length)
    )

    logger.info(f"Generated random email: {email}")
    logger.info(f"Generated random password: {rand_password}")

    return {"email": email, "password": rand_password}
